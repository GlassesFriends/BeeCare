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
    # |=| Registro de nuevos avistamientos.                   |=|
    path('sighting-map/', views.sightingMember, name='sighting-map'),
    # |=| Json de get_Sighting .                              |=|
    path('coord/', views.get_Sighting,name='coord'),
    # |=| Json de get_Bee .                                   |=|
    path('bee/', views.get_Bee,name='bee'),
    # |=| Json de get_Family .                                |=|
    path('family/', views.get_Family,name='family'),
    # |=| Json de get_Subfamily.                              |=|
    path('subfamily/', views.get_Subfamily,name='subfamily'),

]