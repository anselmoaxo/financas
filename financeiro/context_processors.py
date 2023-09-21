from .models import Transaction
from django.db.models import Sum


def soma_transacao(request):
    soma_despesas = Transaction.objects.filter(transaction_type="Despesas").aggregate(
        total_soma=Sum("amount")
    )["total_soma"]
    soma_receitas = Transaction.objects.filter(transaction_type="Receita").aggregate(
        total_soma=Sum("amount")
    )["total_soma"]
    saldo = soma_receitas - soma_despesas

    return {
        "soma_despesas": soma_despesas,
        "soma_receita": soma_receitas,
        "saldo": saldo,
    }
