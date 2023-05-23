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

urlpatterns=[
    path('<int:pk>/',views.formQuestion, name='formnum'),
    path('averageForm/',views.get_Average, name='average')
]