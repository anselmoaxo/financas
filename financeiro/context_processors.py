from .models import Transaction
from django.db.models import Sum


def soma_transacao(request):
    # Filtra todas as Transações de Despesas e Soma o Total
    despesas_result = Transaction.objects.filter(transaction_type="Despesas").aggregate(total_soma=Sum("amount"))
    soma_despesas = despesas_result["total_soma"] if despesas_result["total_soma"] is not None else 0

    # Filtra todas as Transações de Receita e Soma o Total
    receitas_result = Transaction.objects.filter(transaction_type="Receita").aggregate(total_soma=Sum("amount"))
    soma_receitas = receitas_result["total_soma"] if receitas_result["total_soma"] is not None else 0

    # Calcula Receitas - Despesas
    saldo = soma_receitas - soma_despesas

    # Retorna as  Soma_despesas, soma_receitas e Saldo
    return {
        "soma_despesas": soma_despesas,
        "soma_receitas": soma_receitas,
        "saldo": saldo,
    }
