
from django.views.generic import TemplateView
from .forms import UsuarioForm, UpdateForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


class Entrar(TemplateView):
    template_name = 'home.html'


class Registrar(CreateView):
    template_name = "cadastro.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('home')


class UsuarioUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = User
    template_name = 'atualiza_usuario.html'
    form_class = UpdateForm
    success_url = reverse_lazy('home')






