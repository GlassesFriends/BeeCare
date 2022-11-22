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
    # |=| Registro de nuevos avistamientos personales         |=|
    path('sightings/', views.sightingMap, name='sighting-map'),
    # |=| Registros personales de avistamientos.              |=|
    path('sighting-own/', views.sightingMapOwn, name='sighting-own'),
    # |=| Registro de nuevos avistamientos.                   |=|
    path('sighting-reg/', views.sightingRegister, name='sighting-reg'),
    # |=| Json de get_Sighting .                              |=|
    path('coord/', views.get_Sighting,name='coord'),
    # |=| Json de get_Sighting .                              |=|
    path('coord-personal/', views.get_Sighting_Personal,name='coord-personal'),
    # |=| Json de get_General .                              |=|
    path('coord-general/', views.get_Sighting_General,name='coord-general'),
    # |=| Json de get_Bee .                                   |=|
    path('bee/', views.get_Bee,name='bee'),
    # |=| Json de get_Family .                                |=|
    path('family/', views.get_Family,name='family'),
    # |=| Json de get_Subfamily.                              |=|
    path('subfamily/', views.get_Subfamily,name='subfamily'),

]