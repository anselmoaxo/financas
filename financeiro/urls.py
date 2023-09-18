from django.urls import path, reverse_lazy
from financeiro import views
from django.contrib.auth import views as auth_view

app_name = "filme"

urlpatterns = [
    path("", views.Homepage.as_view(), name="index"),
]
