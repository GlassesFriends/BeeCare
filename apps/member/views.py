# |=============================================================|
# |===============|         BIBLIOTECAS         |===============|
# |=============================================================|

# |=========================================|
# |=====|       BIBLIOTECAS BASE      |=====|
# |=========================================|
from django.shortcuts import render
from django.http import HttpResponse
from django.forms import inlineformset_factory

# |=========================================|
# |=====|       BIBLIOTECAS BASE      |=====|
# |=========================================|
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages

# |=========================================|
# |=====|     BIBLILIOTECAS EXTRAS    |=====|
# |=========================================|
from datetime import datetime, date, timedelta

# |=============================================================|
# |===============|    COMIENZAN VARIABLES      |===============|
# |=============================================================|
current_week = date.today().isocalendar()[1] 

# |=============================================================|
# |===============|      COMIENZAN VISTAS       |===============|
# |=============================================================|

# |=========================================|
# |=====|        Home de miembros     |=====|
# |=========================================|
# |=| Proceso de Ckech in de trabajador.  |=|
# |=========================================|
def Dashboard(request):
    
    context = {
        'home': 'active',
        }
    return render(request, 'member/home.html', context)