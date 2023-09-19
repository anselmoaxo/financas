from django.shortcuts import render
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


class CadastroTransacao(CreateView):
    template_name = "cadastro.html"
    model = Transaction
    fields = "__all__"
    success_url = reverse_lazy("financeiro:lista_transacao")


class ListaTransacao(ListView):
    model = Transaction
    template_name = "lista_transacao.html"


class UpdateTransacao(UpdateView):
    template_name = "cadastro.html"
    model = Transaction
    fields = "__all__"
    success_url = reverse_lazy("financeiro:lista_transacao")


class DeleteTransacao(DeleteView):
    template_name = "excluir_transacao.html"
    model = Transaction
    success_url = reverse_lazy("financeiro:lista_transacao")
