from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)
from .models import Transaction, Category
from django.urls import reverse_lazy


class Homepage(TemplateView):
    template_name = "index.html"


class CadastroTransacao(LoginRequiredMixin, CreateView):
    template_name = "cadastro.html"
    model = Transaction
    fields = "__all__"
    success_url = reverse_lazy("financeiro:lista_transacao")


class ListaTransacao(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = "lista_transacao.html"


class UpdateTransacao(LoginRequiredMixin, UpdateView):
    template_name = "cadastro.html"
    model = Transaction
    fields = "__all__"
    success_url = reverse_lazy("financeiro:lista_transacao")


class DeleteTransacao(LoginRequiredMixin, DeleteView):
    template_name = "excluir_transacao.html"
    model = Transaction
    success_url = reverse_lazy("financeiro:lista_transacao")
