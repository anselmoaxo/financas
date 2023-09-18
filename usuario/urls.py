from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name='reset_password.html'
    ), name="reset_password"),
    # Modulo Usuário
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html'
    ), name="login"),
    path('home/', views.Entrar.as_view(), name="home"),
    #Modulo Usuário
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html'
    ), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('cadastro/', views.Registrar.as_view(), name="cadastro"),
    path('atualiza_usuario/<int:pk>/', views.UsuarioUpdate.as_view(), name='atualiza_usuario'),
    path('atualiza_usuario/', auth_views.PasswordChangeView.as_view(
        template_name='atualiza_usuario.html'),
         name='atualiza_usuario'),

]
