from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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

        # Busca pelo botão de filtro
        filtro_form = FiltrarLivrosForm(self.request.GET)
        if filtro_form.is_valid():
            queryset = queryset.filter(**{k: v for k, v in filtro_form.cleaned_data.items() if v})

        return queryset


class AdicionarLivroView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Livros
    form_class = AdicionarLivrosForm
    template_name = 'livro/adicionar_livro.html'
    login_url = '/login/'
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
            return '/login/'
        return super().get_redirect_url()


class DetalhesLivroView(DetailView):
    model = Livros
    template_name = 'book.html'
    context_object_name = 'livro'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ComentarLivroForm()  # Pass the form to the template
        
        livro = self.get_object()
        context['comentarios'] = Comentario.objects.filter(livro=livro).order_by('-postado_em')  # Show comments, ordered by date
        
        return context
    
    def get_object(self):
        slug = self.kwargs['slug']
        return get_object_or_404(Livros, slug=slug)

    def post(self, request, *args, **kwargs):
        livro = self.get_object()
        
        if request.user.is_authenticated:
            form = ComentarLivroForm(request.POST)
            
            if form.is_valid():
                comentario = form.save(commit=False)
                comentario.usuario = request.user.usuario  # Atribui o usuario atual
                comentario.livro = livro  # Atribui o livro atual
                comentario.save()
                return self.get(request, *args, **kwargs)  # Recarrega a página após a postagem
        else:
            # Se o usuario não estiver logado, encaminha para a tela de login
            return redirect(f'{reverse("login")}?next={request.path}')

        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)

class FavoritarLivroView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users_app:user-login')

    def post(self, request, *args, **kwargs):
        # recuperar usuario
        usuario = request.user.usuario
        livro = Livros.objects.get(id=self.kwargs['pk'])
        # registramos favorito
        Favoritos.objects.create(
            usuario=usuario,
            livro=livro,
        )

        return self.get(request, *args, **kwargs)


class DesfavoritarLivroView(DeleteView):
    model = Favoritos
    success_url = '.'
