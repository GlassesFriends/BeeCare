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
from .decorators import user_auth, allowed_users
from apps.member.forms import CreateUserForm, CreateMemberForm

# |=========================================|
# |=====|     REFERENCIAS A MODELOS   |=====|
# |=========================================|
from apps.member.models import member

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

# |=========================================|
# |=====| Cierre de sesión de miembro |=====|
# |=========================================|
# |=| Solo se trata de la ruta a la que   |=|
# |=| se hace referencia para cerrar la   |=|
# |=| sesión del usuario registrado.      |=|
# |=========================================|
@user_auth
def workerLogout(request):
    logout(request)
    return redirect('workerLogin')


# |=========================================|
# |=====|    REGISTRO DE MIEMBROS     |=====|
# |=========================================|
# | =-=|  Administradores y el dpto de |=-= |
# | =-=|  sistemas.                    |=-= |
# |=========================================|
# |=| Registro de miembros.               |=|
# |=| Estos se registrarán con el grupo   |=|
# |=| de trabajadores 'member' por        |=|
# |=| defecto.                            |=|
# |=========================================|

# |=========================================|
# |=|    AL INICIAR POR PRIMERA VEZ EL    |=|
# |=|              SISTEMA                |=|
# |=========================================|
# |=| Cuando se inicie por primera vez el |=|
# |=| sistema se deberá ejecutar el sig.  |=|
# |=| conjunto de lineas respecto al      |=|
# |=| primer usuario registrado, en otras |=|
# |=| palabras, el correo del primer      |=|
# |=| usuario deberá tener permisos de    |=|
# |=| super usuario.                      |=|
# |=========================================|

# python manage.py shell
# from django.contrib.auth.models import User
# user = User.objects.get(username="a.gonzalez@glassesfriends.com")
# user.is_staff = True
# user.is_superuser = True
# user.save()
# exit()

# |=========================================|
# |=|           REFERENCIAS               |=|
# |=========================================|
# https://docs.djangoproject.com/en/4.1/ref/contrib/auth/
# https://stackoverflow.com/questions/11337420/can-i-use-an-existing-user-as-django-admin-when-enabling-admin-for-the-first-tim

# @user_auth
# @allowed_users(allowed_roles=['admin'])
def memberRegister(request):
    
    # |=| Inicializamos una instancia del |=|
    # |=| formulario para registrar un    |=|
    # |=| usuario.                        |=|
    form = CreateUserForm()
    
    # |=| Validamos el método de nuestro  |=|
    # |=| formulario.                     |=|
    if request.method == 'POST':
        userForm = CreateUserForm(request.POST)
        if userForm.is_valid():
            # |=| Capturamos los datos del|=|
            # |=| formulario.             |=|
            user = userForm.save()
            username = userForm.cleaned_data.get('username')
            email = userForm.cleaned_data.get('username')
            first_name = userForm.cleaned_data.get('first_name')
            last_name = userForm.cleaned_data.get('last_name')
            print(request.POST.get('membDateBirth'))
            print(request.POST.get('membPhone'))
            print(request.POST.get('membProfilePicture'))
            
            # |=| Asignamos el grupo      |=|
            # |=| 'member' al nuevo user. |=|
            group, created  = Group.objects.get_or_create(name ='member')
            user.groups.add(group)
            
            # |=| Creamos nuestro objeto  |=|
            # |=| de nuestra tabla de     |=|
            # |=| relación OneToOne con la|=|
            # |=| tabla de users de       |=|
            # |=| django.                 |=|
            member.objects.create(
                membFirstName =         user.first_name,
                membLastName =          user.last_name,
                
                # |=| Se obtiene la data  |=|
                # |=| del formulario por  |=|
                # |=| medio del método    |=|
                # |=| request.            |=|
                membDateBirth =         request.POST.get('membDateBirth'),
                membPhone =             request.POST.get('membPhone'),
                membProfilePicture =    request.POST.get('membProfilePicture'),
                
                membEmail =             user.username,
                membUser =              user,
            )
            
            # |=| Cuando finaliza el      |=|
            # |=| registro, se redirije al|=|
            # |=| usuario a nuestra pag.  |=|
            # |=| de inicio de sesión.    |=|
            text = 'Please, sign in'
            messages.success(request, text)
            
    context = {
        'signUp': 'active',
        'form': form,
        }
    return render(request, 'member/signup.html', context)