# |=============================================================|
# |===============|         BIBLIOTECAS         |===============|
# |=============================================================|

# |=========================================|
# |=====|       BIBLIOTECAS BASE      |=====|
# |=========================================|
from django.contrib import admin
from django.urls import path

# |=| Biblioteca que permite redireccionar|=|
from . import views

urlpatterns = [
    # |=| Página principal de la wiki, donde se muestra la lista de artículos. |=|
    path('', views.wikihome, name='wikihome'),
    path('<slug:bPostSlug>/', views.article_detail, name='article_detail'),
]