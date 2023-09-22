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


class DeleteTransacao(LoginRequiredMixin, DeleteView):
    template_name = "excluir_transacao.html"
    model = Transaction
    success_url = reverse_lazy("financeiro:lista_transacao")


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


# Função para criar o gráfico de barras
def create_bar_chart():
    # Chama a função soma_transacao, que retorna um contexto com informações de despesas e receitas
    transacao_context = soma_transacao(
        None
    )  # Você pode passar None para request, pois não está usando em soma_transacao

    # Obtém os valores de despesas e receitas a partir do contexto
    soma_despesas = transacao_context["soma_despesas"]
    soma_receitas = transacao_context["soma_receita"]

    # Define os rótulos (labels) e os valores para o gráfico
    labels = ["Despesas", "Receita"]
    values = [soma_despesas, soma_receitas]
    destaques = [0.05, 0.05]
    # Cria o gráfico de barras
    plt.pie(values, labels=labels, autopct="%1.f", explode=destaques, shadow=True)

    # Adiciona rótulos e título ao gráfico
    plt.title("Percentual Despesas/Receita")
    # Salva o gráfico como um arquivo de imagem PNG
    plt.savefig("static/bar_chart.png")


# Função que retorna a imagem do gráfico como resposta HTTP
def chart_image(request):
    # Chama a função para criar o gráfico
    create_bar_chart()

    # Define o caminho completo para a imagem gerada
    image_path = os.path.join(settings.STATIC_ROOT, "bar_chart.png")

    # Abre o arquivo de imagem em modo de leitura binária
    with open(image_path, "rb") as f:
        # Retorna a imagem como uma resposta HTTP com o tipo de conteúdo "image/png"
        return HttpResponse(f.read(), content_type="image/png")
