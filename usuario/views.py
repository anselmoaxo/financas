from django.views.generic import TemplateView
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


class Registrar(CreateView):
    template_name = "cadastro_user.html"
    form_class = UsuarioForm
    success_url = reverse_lazy("financeiro:index")


class UsuarioUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("login")
    model = User
    template_name = "atualiza_usuario.html"
    fields = ["first_name", "last_name", "email"]
    success_url = reverse_lazy("financeiro:index")
