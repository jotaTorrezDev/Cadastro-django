from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    # rota, view responsavel, nome de referencia
    #pagina inicial
    path('',views.home,name='home'),
    #usuarios.com/usuarios
    path('usuarios/',views.usuarios,name='listagem_de_usuarios')
]