from django.contrib.auth.models import Group
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from django.views.generic import TemplateView, FormView

from apps.usuario.forms import RegistrarUsuarioForm
from apps.usuario.models import Usuario, Favoritos

class HomePage(TemplateView):
    template_name = "home.html"


class RegistrarUsuarioView(FormView):
    template_name = 'login.html'
    form_class = RegistrarUsuarioForm

    def form_valid(self, form):
        user = form.save()

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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_registrar'] = kwargs.get('form_registrar', RegistrarUsuarioForm(prefix="form1"))
        context['form_login'] = kwargs.get('form_login', AuthenticationForm(prefix="form2"))
        return context

    def post(self, request, *args, **kwargs):
        form_registrar = RegistrarUsuarioForm(request.POST, prefix="form1")
        form_login = AuthenticationForm(request, data=request.POST, prefix="form2")  # Request para o form de login

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
        favoritos = Favoritos.usuario.get(usuario)

        context = super().get_context_data(**kwargs)
        context = {
            'username': username,
            'usuario': usuario,
            'favoritos': favoritos
        }
        return context