from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

app_name = "usuario"

urlpatterns = [
    path(
        "login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"
    ),
    # Modulo Usuário
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("cadastro_user/", views.Registrar.as_view(), name="cadastro_user"),
    path(
        "atualiza_usuario/<int:pk>/",
        views.UsuarioUpdate.as_view(),
        name="atualiza_usuario",
    ),
    path(
        "atualiza_usuario/",
        auth_views.PasswordChangeView.as_view(template_name="atualiza_usuario.html"),
        name="atualiza_usuario",
    ),
]
