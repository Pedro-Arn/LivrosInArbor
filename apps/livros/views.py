# Importação des bibliotecas de restrições de acessos
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Importação de uma biblioteca de paginação
from django.core.paginator import Paginator
from django.db.models import Case, When, Value, IntegerField, Q
from django.http import HttpResponseForbidden, JsonResponse
# Importação da função que exibe erro 404
from django.shortcuts import get_object_or_404, redirect
# Importação da função que gera URL'S dinamicamente
from django.urls import reverse_lazy, reverse
# Importação de classes para construir view
from django.views.generic import (
    CreateView,
    DetailView,
    ListView, 
    View,
)
# Importação de formulários relacionados ao livro
from apps.livros.forms import (
    AdicionarLivrosForm,
    ComentarLivroForm,
)
# Importação de classes de associação
from apps.livros.models import Livros, Comentario, Link
from apps.usuario.models import Favoritos

# Criação da classe 'ListarLivrosView' 
class ListarLivrosView(ListView):
    model = Livros # Faz a chamada do modelo que a corresponde
    template_name = 'search.html' # Faz a chamada da tela que a corresponde
    context_object_name = 'livros' # Nome da variável de acesso ao conjunto
    paginate_by = 10 # Quantidade de respostas na tela
 
    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search_query', '').strip()
        ano_publicacao = self.request.GET.get('ano_publicacao', '').strip()
        editora = self.request.GET.get('editora', '').strip()
        materia = self.request.GET.get('materia', '').strip()
        curso = self.request.GET.get('curso', '').strip()
        periodo = self.request.GET.get('periodo', '').strip()

        # # Caso haja um termo de busca a função apply é chamada
        if search_query:
            queryset = self.apply_search_query(queryset, search_query)

        # Insere filtros adicionais por atributos
        queryset = self.apply_filters(queryset)

        # Apply filters
        if ano_publicacao:
            queryset = queryset.filter(ano_publicacao=ano_publicacao)
        if editora:
            queryset = queryset.filter(editora__nome__icontains=editora)
        if materia:
            queryset = queryset.filter(materia__nome__icontains=materia)
        if curso:
            queryset = queryset.filter(materia__cursos__nome__icontains=curso)  # Traverse through Materias to Cursos
        if periodo:
            queryset = queryset.filter(materia__periodo=periodo)  # Filter by periodo in Materias
        
        # Previnir resultados repetidos
        queryset = queryset.distinct()

        return queryset

    def apply_search_query(self, queryset, search_query):
        # Definição de atributos de busca
        return queryset.filter(
            Q(titulo__icontains=search_query) |
            Q(autor__nome_completo__icontains=search_query)
        )

    def apply_filters(self, queryset):
        filters = {}

        # Filtro por ano
        ano_publicacao = self.request.GET.get('ano_publicacao')
        if ano_publicacao:
            filters['ano_publicacao'] = ano_publicacao

        # Filtro por editora
        editora = self.request.GET.get('editora')
        if editora:
            filters['editora__nome__icontains'] = editora

        # Filtro por matéria
        materia = self.request.GET.get('materia')
        if materia:
            filters['materia__nome__icontains'] = materia
        
        # Filtro por período
        periodo = self.request.GET.get('periodo')
        if periodo:
            # Acessando curso através de materia
            filters['materia__periodo'] = periodo

        # Filtro por curso
        curso = self.request.GET.get('curso')
        if curso:
            # Acessando curso através de materia
            filters['materia__cursos__nome__icontains'] = curso

        return queryset.filter(**filters)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search_query', '')
        context['ano_publicacao'] = self.request.GET.get('ano_publicacao', '')
        context['editora'] = self.request.GET.get('editora', '')
        context['materia'] = self.request.GET.get('materia', '')
        context['periodo'] = self.request.GET.get('periodo', '')
        context['curso'] = self.request.GET.get('curso', '')
        return context

class AdicionarLivroView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Livros
    form_class = AdicionarLivrosForm
    template_name = 'adicionarLivro.html'
    login_url = 'usuario:login'
    success_url = '.'

    def form_valid(self, form):
        # Salva o livro adicionado
        self.object = form.save()

        # Process new links
        new_links = form.cleaned_data.get('new_links', '').strip()
        if new_links:
            for line in new_links.split('\n'):
                if line.strip():
                    site, link = line.strip().split(',', 1)
                    link_obj, created = Link.objects.get_or_create(site=site.strip(), link=link.strip())
                    self.object.links.add(link_obj)

        return redirect(self.get_success_url())

    def form_invalid(self, form):
        return super().form_invalid(form)

    def test_func(self):
        # Permite acesso se o usuário for superuser ou estiver no grupo 'professor'
        user = self.request.user
        return user.is_superuser or user.groups.filter(name='professor').exists()

    def get_redirect_url(self):
        # Se não for professor, redireciona para outra pagina
        if not self.test_func():
            return 'usuario:home'
        return super().get_redirect_url()


class DetalhesLivroView(DetailView):
    model = Livros
    template_name = 'livro.html'
    context_object_name = 'livro'
    login_url = 'usuario:login'
    sucess_url = '.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ComentarLivroForm()  # Form para comentarios
        
        livro = self.get_object()
        comentarios_list = Comentario.objects.filter(livro=livro).annotate(
        tipo_ordem=Case(
            When(usuario__tipo_identificacao='P', then=Value(1)),  # Professores primeiro
            When(usuario__tipo_identificacao='E', then=Value(2)),  # Estudantes depois
            default=Value(3),
            output_field=IntegerField()
        )
        ).order_by('tipo_ordem', '-postado_em')

        # Paginação
        paginator = Paginator(comentarios_list, 5)  # Define 5 comentários por página
        page = self.request.GET.get('page')
        comentarios = paginator.get_page(page)

        context['comentarios'] = comentarios

        if self.request.user.is_authenticated and hasattr(self.request.user, 'usuario'):
            context['is_favorited'] = Favoritos.objects.filter(livro=livro, usuario=self.request.user.usuario).exists()
        else:
            context['is_favorited'] = False

        return context
    
    def get_object(self):
        slug = self.kwargs['slug']
        return get_object_or_404(Livros, slug=slug)

    def post(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            # Se o usuário é um administrador, não terá permissão para comentar no livro
            return HttpResponseForbidden("Você não tem permissão para comentar.")

        livro = self.get_object()
        
        comentario_id = request.POST.get("comentario_id")
        if comentario_id:
            return self.excluir_comentario(request, comentario_id)

        if request.user.is_authenticated:
            form = ComentarLivroForm(request.POST)
            
            if form.is_valid():
                comentario = form.save(commit=False)
                comentario.usuario = request.user.usuario  # Atribui o usuario atual
                comentario.livro = livro  # Atribui o livro atual
                comentario.save()
                return redirect(request.path)  # Recarrega a página após a postagem
        else:
            # Se o usuario não estiver logado, encaminha para a tela de login
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
            # Se o usuário é um administrador, não terá permissão para favoritar o livro
            return HttpResponseForbidden("Você não tem permissão para favoritar este livro.")

        usuario = request.user.usuario
        livro = get_object_or_404(Livros, id=self.kwargs['pk'])

        # Retorna ou cria uma instância de favorito
        favorito, created = Favoritos.objects.get_or_create(usuario=usuario, livro=livro)
        
        if not created:  
            # Se já existir, desfavorita
            favorito.delete()

        # Redireciona de volta à pagina de detalhes do livro
        return redirect(reverse('livros:detalhes_livro', kwargs={'slug': livro.slug}))