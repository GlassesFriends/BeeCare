# |=============================================================|
# |===============|         BIBLIOTECAS         |===============|
# |=============================================================|

# |=========================================|
# |=====|       BIBLIOTECAS BASE      |=====|
# |=========================================|
from django.contrib import admin
from django.urls import path, include

# |=========================================|
# |=====|   BIBLIOTECAS ADICIONALES   |=====|
# |=========================================|

# |=| Biblioteca que permite redireccionar|=|
from . import views

# |=| Biblioteca que permite redireccionar|=|
from django.shortcuts import redirect

# |=============================================================|
# |===============|        Lista de URLs        |===============|
# |=============================================================|

urlpatterns = [
    # |=| Dashboard de miembros.              |=|
    path('', views.Dashboard, name='home'),
    # |=| Registro de nuevos miembros         |=|
    path('signup', views.memberRegister, name='signup'),
]
