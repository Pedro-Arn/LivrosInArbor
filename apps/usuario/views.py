from django.contrib.auth.models import Group, User
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages

from django.views.generic import TemplateView, FormView

from apps.usuario.forms import RegistrarUsuarioForm


class HomePage(TemplateView):
    template_name = "home.html"


class RegistrarUsuarioView(FormView):
    template_name = 'login.html'
    form_class = RegistrarUsuarioForm
    # success_url = reverse_lazy('home')

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
        form_login = AuthenticationForm(request, data=request.POST, prefix="form2")  # Pass `request` for login form

        if form_registrar.is_valid():
            # Handle registration logic
            user = form_registrar.save()

            ocupacao = form_registrar.cleaned_data['ocupacao']
            group_name = 'Professor' if ocupacao == 'P' else 'Geral'
            group, _ = Group.objects.get_or_create(name=group_name)
            user.groups.add(group)

            login(request, user)
            return HttpResponseRedirect(reverse_lazy('home'))

        elif form_login.is_valid():
            # Handle login logic
            user = form_login.get_user()
            login(request, user)
            return HttpResponseRedirect(reverse_lazy('home'))

        # If forms are invalid, re-render the page with errors
        return self.render_to_response(self.get_context_data(form_registrar=form_registrar, form_login=form_login))
        
class LoginUsuarioView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    redirect_authenticated_user = True  # Redireciona usuarios logados

    def get_success_url(self):
        messages.success(self.request, "Login successful.")
        return reverse_lazy('home')


class PerfilUsuarioView(TemplateView):
    template_name = 'usuario/perfil.html'

    def get_context_data(self, **kwargs):
        username = self.kwargs['username']
        user = get_object_or_404(User, username=username)

        if self.request.user != user:
            # Redirect or return an error message if needed
            # For now, just display a message or handle accordingly
            raise PermissionError("You don't have permission to view this profile.")

        context = super().get_context_data(**kwargs)
        context['user_profile'] = user  # Add user profile to the context
        return context