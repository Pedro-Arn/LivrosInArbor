from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django.db.models import Case, When, Value, IntegerField
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView, 
    View,
)

from apps.livros.forms import (
    FiltrarLivrosForm,
    AdicionarLivrosForm,
    ComentarLivroForm,
)
from apps.livros.models import Livros, Comentario, Favoritos

class ListarLivrosView(ListView):
    model = Livros
    template_name = 'search.html'
    context_object_name = 'livros'
    paginate_by = 10

    def get_queryset(self):
        search_query = self.request.GET.get('search_query', '').strip()

        queryset = Livros.objects.all()

        # Busca no search
        if search_query:
            queryset = Livros.objects.search_query(search_query)
        else:
            return redirect('usuario:home')

        # Busca pelo botão de filtro
        filtro_form = FiltrarLivrosForm(self.request.GET)
        if filtro_form.is_valid():
            queryset = queryset.filter(**{k: v for k, v in filtro_form.cleaned_data.items() if v})

        return queryset


class AdicionarLivroView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Livros
    form_class = AdicionarLivrosForm
    template_name = 'adicionar_livro.html'
    login_url = 'usuario:login'
    success_url = '.'

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def test_func(self):
        # Limita apenas professores a terem acesso a essa tela
        return self.request.user.groups.filter(name='professor').exists()

    def get_redirect_url(self):
        # Se não for professor, redireciona para outra pagina
        if not self.test_func():
            return 'usuario:home'
        return super().get_redirect_url()


class DetalhesLivroView(DetailView):
    model = Livros
    template_name = 'book.html'
    context_object_name = 'livro'

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
        return context
    
    def get_object(self):
        slug = self.kwargs['slug']
        return get_object_or_404(Livros, slug=slug)

    def post(self, request, *args, **kwargs):
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


class AlternarFavoritosLivroView(LoginRequiredMixin, View):
    login_url = reverse_lazy('usuario:login')

    def post(self, request, *args, **kwargs):
        usuario = request.user.usuario
        livro = get_object_or_404(Livros, id=self.kwargs['pk'])

        # Retorna ou cria uma instancia de favorito
        favorito, created = Favoritos.objects.get_or_create(usuario=usuario, livro=livro)
        
        if not created:  
            # Se já existir, desfavorita
            favorito.delete()
