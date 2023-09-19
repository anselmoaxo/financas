from django.urls import path, reverse_lazy
from financeiro import views
from django.contrib.auth import views as auth_view

app_name = "financeiro"

urlpatterns = [
    path("", views.Homepage.as_view(), name="index"),
    path("cadastro", views.CadastroTransacao.as_view(), name="cadastro"),
    path("lista_transacao", views.ListaTransacao.as_view(), name="lista_transacao"),
    path(
        "update_transacao/<int:pk>/",
        views.UpdateTransacao.as_view(),
        name="update_transacao",
    ),
    path(
        "excluir_transacao/<int:pk>/",
        views.DeleteTransacao.as_view(),
        name="excluir_transacao",
    ),
]
