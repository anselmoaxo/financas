from django.shortcuts import render, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)
from django.conf import settings
import os
from .models import Transaction, Category
from django.urls import reverse_lazy
import matplotlib.pyplot as plt
import matplotlib
from django.db.models import Sum
from financeiro.context_processors import soma_transacao
from django.urls import reverse
from django.shortcuts import get_object_or_404

matplotlib.use("Agg")


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


class DeleteTransacao(DeleteView):
    def get_object(self):
        id = self.kwargs.get('pk')
        return get_object_or_404(Transaction, pk=id)
    
    def get_success_url(self):
        return reverse('financeiro:dashboard')


class ListaDashboard(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = "dashboard.html"


def list_despesas(request):
    lista = Transaction.objects.filter(transaction_type="Despesas")
    context = {"lista": lista}
    return render(request, "lista_despesa.html", context)


def list_receita(request):
    lista = Transaction.objects.filter(transaction_type="Receita")
    context = {"lista": lista}
    return render(request, "lista_receita.html", context)

