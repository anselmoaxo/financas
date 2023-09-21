from django.db import models

from django.db import models

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    description = models.TextField(blank=True, verbose_name="Descrição")

    def __str__(self):
        return self.name


class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ("Despesas", "Despesa"),
        ("Receita", "Receita"),
    ]

    description = models.CharField(
        max_length=255, verbose_name="Descrição da Transação"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Categoria"
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor")
    transaction_date = models.DateField(verbose_name="Data do Pagamento")
    transaction_type = models.CharField(
        max_length=10, choices=TRANSACTION_TYPES, verbose_name="Tipo da Transação"
    )

    def __str__(self):
        return self.description
