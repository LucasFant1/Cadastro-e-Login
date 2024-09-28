
from django.urls import path
from app_cad_usuarios import views  # Importando apenas uma vez, da aplicação correta

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('usuarios/', views.usuarios, name='listagem_usuarios'),  # Listagem de usuários
    path('home/', views.home, name='cadastro'),  # Página de cadastro
    path('login/', views.login, name='login'),  # Página de login
]

