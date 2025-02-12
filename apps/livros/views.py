from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django.db.models import Case, When, Value, IntegerField, Q
from django.http import HttpResponseForbidden, JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView, 
    View,
)

from apps.livros.forms import (
    FiltrarLivrosForm,
    AdicionarLivrosForm,
    ComentarLivroForm,
)
from apps.livros.models import Livros, Comentario, Link
from apps.usuario.models import Favoritos

class ListarLivrosView(ListView):
    model = Livros
    template_name = 'search.html'
    context_object_name = 'livros'
    paginate_by = 10  # Definir a paginação para exibir 10 livros por página

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search_query', '').strip()
        ano_publicacao = self.request.GET.get('ano_publicacao', '').strip()
        editora = self.request.GET.get('editora', '').strip()
        materia = self.request.GET.get('materia', '').strip()
        curso = self.request.GET.get('curso', '').strip()
        periodo = self.request.GET.get('periodo', '').strip()

        # Aplicar a pesquisa por título, autor ou editora
        if search_query:
            queryset = self.apply_search_query(queryset, search_query)

        # Aplicar filtros
        if ano_publicacao:
            queryset = queryset.filter(ano_publicacao=ano_publicacao)
        if editora:
            queryset = queryset.filter(editora__nome__icontains=editora)
        if materia:
            queryset = queryset.filter(materia__nome__icontains=materia)
        if curso:
            queryset = queryset.filter(materia__cursos__nome__icontains=curso)
        if periodo:
            queryset = queryset.filter(materia__periodo=periodo)

        return queryset

    def apply_search_query(self, queryset, search_query):
        """
        Aplica a pesquisa ao queryset.
        """
        return queryset.filter(
            Q(titulo__icontains=search_query) |
            Q(autor__nome_completo__icontains=search_query) |
            Q(editora__nome__icontains=search_query) |
            Q(materia__nome__icontains=search_query)
        )

    def get_context_data(self, **kwargs):
        """
        Passa os dados da pesquisa e dos filtros para o template.
        """
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search_query', '')
        context['ano_publicacao'] = self.request.GET.get('ano_publicacao', '')
        context['editora'] = self.request.GET.get('editora', '')
        context['materia'] = self.request.GET.get('materia', '')
        context['curso'] = self.request.GET.get('curso', '')
        context['periodo'] = self.request.GET.get('periodo', '')
        context['filtro_form'] = FiltrarLivrosForm(self.request.GET)
        return context


class AdicionarLivroView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Livros
    form_class = AdicionarLivrosForm
    template_name = 'adicionarLivro.html'
    login_url = 'usuario:login'
    success_url = '.'

    def form_valid(self, form):
        # Salva o livro primeiro
        self.object = form.save()

        # Processa novos links
        new_links = form.cleaned_data.get('new_links', '').strip()
        if new_links:
            for line in new_links.split('\n'):
                if line.strip():
                    site, link = line.strip().split(',', 1)
                    link_obj, created = Link.objects.get_or_create(site=site.strip(), link=link.strip())
                    self.object.links.add(link_obj)

        return redirect(self.get_success_url())

    def test_func(self):
        # Permite acesso se o usuário for superusuário ou estiver no grupo 'professor'
        user = self.request.user
        return user.is_superuser or user.groups.filter(name='professor').exists()


class DetalhesLivroView(DetailView):
    model = Livros
    template_name = 'livro.html'
    context_object_name = 'livro'
    login_url = 'usuario:login'
    sucess_url = '.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ComentarLivroForm()  # Formulário para comentários
        
        livro = self.get_object()
        comentarios_list = Comentario.objects.filter(livro=livro).annotate(
        tipo_ordem=Case(
            When(usuario__tipo_identificacao='P', then=Value(1)),  # Professores primeiro
            When(usuario__tipo_identificacao='E', then=Value(2)),  # Estudantes depois
            default=Value(3),
            output_field=IntegerField()
        )
        ).order_by('tipo_ordem', '-postado_em')

        # Paginação dos comentários (5 por página)
        paginator = Paginator(comentarios_list, 5)
        page = self.request.GET.get('page')
        comentarios = paginator.get_page(page)

        context['comentarios'] = comentarios

        # Verifica se o livro está favoritado pelo usuário
        if self.request.user.is_authenticated and hasattr(self.request.user, 'usuario'):
            context['is_favorited'] = Favoritos.objects.filter(livro=livro, usuario=self.request.user.usuario).exists()
        else:
            context['is_favorited'] = False

        return context
    
    def get_object(self):
        # Obtém o livro com base no slug
        slug = self.kwargs['slug']
        return get_object_or_404(Livros, slug=slug)

    def post(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            # Se o usuário for administrador, não poderá comentar no livro
            return HttpResponseForbidden("Você não tem permissão para comentar.")

        livro = self.get_object()
        
        comentario_id = request.POST.get("comentario_id")
        if comentario_id:
            return self.excluir_comentario(request, comentario_id)

        if request.user.is_authenticated:
            form = ComentarLivroForm(request.POST)
            
            if form.is_valid():
                comentario = form.save(commit=False)
                comentario.usuario = request.user.usuario  # Atribui o usuário atual
                comentario.livro = livro  # Atribui o livro atual
                comentario.save()
                return redirect(request.path)  # Recarrega a página após a postagem
        else:
            # Se o usuário não estiver logado, redireciona para a tela de login
            return redirect(f'{reverse("usuario:login")}?next={request.path}')

        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)
    
    def excluir_comentario(self, request, comentario_id):
        comentario = get_object_or_404(Comentario, id=comentario_id)

        # Verifica se o usuário tem permissão para excluir o comentário
        if request.user.usuario != comentario.usuario:
            return HttpResponseForbidden("Você não tem permissão para excluir este comentário.")

        comentario.delete()
        return redirect(request.path)


class AlternarFavoritosView(LoginRequiredMixin, View):
    login_url = reverse_lazy('usuario:login')

    def post(self, request, *args, **kwargs):
        if not hasattr(request.user, 'usuario'):
            # Se o usuário for administrador, não poderá favoritar o livro
            return HttpResponseForbidden("Você não tem permissão para favoritar este livro.")

        usuario = request.user.usuario
        livro = get_object_or_404(Livros, id=self.kwargs['pk'])

        # Obtém ou cria uma instância de favorito
        favorito, created = Favoritos.objects.get_or_create(usuario=usuario, livro=livro)
        
        if not created:  
            # Se já existir, desfavorita
            favorito.delete()

        # Redireciona de volta para a página de detalhes do livro
        return redirect(reverse('livros:detalhes_livro', kwargs={'slug': livro.slug}))
