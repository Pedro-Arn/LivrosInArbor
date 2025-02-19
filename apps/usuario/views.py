# Importação do modelo de grupos de usuários do Django
from django.contrib.auth.models import Group
# Importação da função de autenticação o usuário 
from django.contrib.auth import login
# Importação do formulário de autenticação o usuário 
from django.contrib.auth.forms import AuthenticationForm
# Importação de redirecionamento após ação
from django.http import HttpResponseRedirect
# Importação de exibição de erro 404
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
# Importação de views genéricas
from django.views.generic import TemplateView, FormView
# Importação de classes-formulários de associação
from apps.usuario.forms import (
    RegistrarUsuarioForm, 
    EditarPerfilForm,
    GerenciarFavoritosForm,
    )
# Importação de classes de associação
from apps.usuario.models import Usuario, Favoritos

# Exibe tela inicial
class HomePage(TemplateView):
    template_name = "home.html"

# Criação da classe 'RegistrarUsuarioView' que faz a chamada do modelo e da tela correspondente a ela
class RegistrarUsuarioView(FormView):
    template_name = 'login.html'
    form_class = RegistrarUsuarioForm

    # Formulário de registro validado
    def form_valid(self, form):
        user = form.save() # Salva usuário no BD

        ocupacao = form.cleaned_data['ocupacao']
        if ocupacao == 'E':
            group_name = 'Geral'
        elif ocupacao == 'P':
            group_name = 'Professor'
        else:
            group_name = 'Geral'

        if group_name:
            group = Group.objects.get_or_create(name=group_name)
            user.groups.add(group.id)
        
        login(self.request, user)
        return super().form_valid(form)
    
    # Passa informações para o template renderizado
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_registrar'] = kwargs.get('form_registrar', RegistrarUsuarioForm(prefix="form1"))
        context['form_login'] = kwargs.get('form_login', AuthenticationForm(prefix="form2"))
        return context
    
    # Processa dados de registro e login
    def post(self, request, *args, **kwargs):
        form_registrar = RegistrarUsuarioForm(request.POST, prefix="form1")
        form_login = AuthenticationForm(request, data=request.POST, prefix="form2") 

        if form_registrar.is_valid():
            # Lógica para registro
            user = form_registrar.save()

            ocupacao = form_registrar.cleaned_data['ocupacao']
            group_name = 'Professor' if ocupacao == 'P' else 'Geral'
            group, _ = Group.objects.get_or_create(name=group_name)
            user.groups.add(group)

            login(request, user)
            return HttpResponseRedirect(reverse_lazy('usuario:home'))

        elif form_login.is_valid():
            # Lógica para login
            user = form_login.get_user()
            login(request, user)
            return HttpResponseRedirect(reverse_lazy('usuario:home'))

        # Se der erro, recarrega a página
        return self.render_to_response(self.get_context_data(form_registrar=form_registrar, form_login=form_login))


class PerfilUsuarioView(TemplateView):
    template_name = 'perfil.html'

    def get_context_data(self, **kwargs):
        username = self.kwargs['username']
        usuario = get_object_or_404(Usuario, username=username)
        favoritos = Favoritos.objects.filter(usuario=usuario).select_related('livro')

        # Adição de formulário ao contexto
        context = super().get_context_data(**kwargs)
        context.update({
            'username': username,
            'usuario': usuario,
            'favoritos': favoritos,
            'editar_perfil_form': EditarPerfilForm(instance=usuario),
            'gerenciar_favoritos_form': GerenciarFavoritosForm(usuario=usuario),
        })
        return context

    # Trata o envio dos formulários de edição e gerenciamento de perfil
    def post(self, request, *args, **kwargs):
        username = self.kwargs['username']
        usuario = get_object_or_404(Usuario, username=username)
        
        # Atualiza as informações do usuário
        if 'editar_perfil' in request.POST:
            form = EditarPerfilForm(request.POST, request.FILES, instance=usuario)
            if form.is_valid():
                form.save() # Salva no BD
                return redirect('perfil', username=username)
        
        # Processa as alterações nos favoritos
        elif 'gerenciar_favoritos' in request.POST:
            form = GerenciarFavoritosForm(usuario=usuario, data=request.POST)
            if form.is_valid():
                form.save() # Salva no BD
                return redirect('perfil', username=username)

        # Caso o formulário seja inválido 
        context = self.get_context_data(**kwargs)
        context['editar_perfil_form'] = form if 'editar_perfil' in request.POST else EditarPerfilForm(instance=usuario)
        context['gerenciar_favoritos_form'] = form if 'gerenciar_favoritos' in request.POST else GerenciarFavoritosForm(usuario=usuario)
        return render(request, self.template_name, context)