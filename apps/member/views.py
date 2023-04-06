# |=============================================================|
# |===============|         BIBLIOTECAS         |===============|
# |=============================================================|

# |=========================================|
# |=====|       BIBLIOTECAS BASE      |=====|
# |=========================================|
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from django.forms import inlineformset_factory

# |=========================================|
# |=====|       BIBLIOTECAS BASE      |=====|
# |=========================================|
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group,User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages

# |=========================================|
# |=====|     BIBLILIOTECAS EXTRAS    |=====|
# |=========================================|
from datetime import datetime, date, timedelta
from .decorators import user_auth, allowed_users
from apps.member.forms import CreateUserForm,UpdateMemberProfile,UpdateJustBasicFilesUser
from apps.formtest.forms import answerusr
from abc import abstractmethod

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
# |=====|        Sobre BeeCare        |=====|
# |=========================================|
# |=| Proceso de Ckech in de trabajador.  |=|
# |=========================================|
def About(request):
    context = {
        'home': 'active',
        }
    return render(request, 'member/about.html', context)

# |=========================================|
# |=====| Cierre de sesión de miembro |=====|
# |=========================================|
# |=| Solo se trata de la ruta a la que   |=|
# |=| se hace referencia para cerrar la   |=|
# |=| sesión del usuario registrado.      |=|
# |=========================================|
# @user_auth
def memberSignOut(request):
    print("No cerre sesión")
    logout(request)
    return redirect('signin')


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
def memberSignUp(request):
    
    # |=| Inicializamos una instancia del |=|
    # |=| formulario para registrar un    |=|
    # |=| usuario.                        |=|
    form = CreateUserForm()
    
    # |=| Validamos el método de nuestro  |=|
    # |=| método POST.                    |=|
    if request.method == 'POST':
        userForm = CreateUserForm(request.POST,request.FILES)
        # |=| Validamos el correo  si es      |=|
        # |=| que este existe.                |=|
        emailtest = request.POST['username']
        # |=| si que este existe.             |=|
        # |=| Retorna una advertencia.        |=|
        if member.objects.filter(membEmail=emailtest).exists():
            messages.warning(request,"El correo que desea registrar ya existe.")
        # |=| si no existe este.             |=|
        # |=| Continua con el formulario.    |=|
        else:
            # |=| Validamos el método de nuestro  |=|
            # |=| formulario.                     |=|    
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
                print(request.FILES.get('membProfilePicture'))
                
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
                    # |=| Usar FILES en lugar |=|
                    # |=| de POST para imagen |=|
                    membProfilePicture =    request.FILES.get('membProfilePicture'),
                    
                    membEmail =             user.username,
                    membUser =              user,
                )
                
                # |=| Cuando finaliza el      |=|
                # |=| registro, se redirije al|=|
                # |=| usuario a nuestra pag.  |=|
                # |=| de inicio de sesión.    |=|
                text = 'Usuario registrado exitosamente, regresa e inicia sesión.'
                messages.success(request, text)
            else:
                messages.error(request,"Error al guardar los datos.")
            
    context = {
        'signUp': 'active',
        }
    return render(request, 'member/signup.html', context)



# |=========================================|
# |=====|    INICIO DE SESIÓN         |=====|
# |=========================================|
# |=| Se muestran los trabajadores que se |=|
# |=| han registrado y estan ACTIVOS ante |=|
# |=| el sistema.                         |=|
# |=========================================|


# |=========================================|
# |========== Main patrón proxy ============|
# |=========================================|

# |===Permite proporcionar un sustituto o===|
# |==marcador de posición para otro objeto.=|
# |==Un proxy controla el acceso al objeto==|
# |===original, permitiéndote hacer algo====|
# |===antes o después de que la solicitud===|
# |========llegue al objeto original========|

def memberSignIn(request):
    # |=| Validamos el formulario actual  |=|
    # |=| respecto al métpdp POST.        |=|
    if request.method == 'POST':
        # |=| Se obtienen los datos del   |=|
        # |=| formulario.                 |=|
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        real_login_access = RealLoginAccess()
        proxy = Proxy(real_login_access)
        if (proxy.Access(request,username,password) == True): 
            # |=| formulario preguntas.            |=|

            iAnswerthetest = answerusr.objects.filter(answerusrMember=request.user.member).count()
            if iAnswerthetest == 0:
                url = reverse('formnum', kwargs={'pk':1})
                return redirect(f'{url}')
            else:
                return redirect(reverse('home'))
            
        else:
            messages.info(request, 'Tu usuario o contraseña es incorrecto, si necesitas ayuda comunicate al departamento de sistemas.')
            
    context = {}
    return render(request, 'member/signin.html', context)

# |============== Servicio ===============|
class LoginAccess():
    @abstractmethod
    def Access(self, request, username, password):
        pass

# |============== Operación ==============|
class RealLoginAccess(LoginAccess):
    def Access(self, request, username, password):
        print('Usuario con correo ' + username + ' logeado correctamente')

# |================ Proxy ================|
class Proxy(LoginAccess):
    def __init__(self, realLoginAccess:RealLoginAccess):  
        self._real_Login_Access = realLoginAccess
    # |========= Access patrón proxy ==========|
    def Access(self,request,username,password):
    # |=| Se activa la sesión.        |=|
        user = authenticate(request, username=username, password=password)
        self._real_Login_Access.Access(request,username,password)
        # |=| Si el trabajador si existe   =|
        # |=| envia directamente a 'home', =|
        if user is not None:
            # |=| Se envia mensaje de      =|
            # |=| bienvenida.              =|
            login(request, user)
            text = 'Bienvenido ' + request.user.member.membFirstName
            messages.success(request, text)
            
            return True
        
        # |=| en caso contrario enviará un =|
        # |=| mensaje de usuario no valido =|
        else:
            False

        

# |=========================================|
# |=====|   ACTUALIZACIÓN DE DATOS    |=====|
# |=========================================|
# |=| Se muestran los avistadores  que se |=|
# |=| han logeado en la página.           |=|
# |=========================================|
@user_auth
def memberUpdate(request):
    # |=| Modelos de actualización de     |=|
    # |=| datos.                          |=|
    profile = member.objects.get(id=request.user.member.pk)
    user_update = User.objects.get(id=request.user.pk)
    user_update_nopass = User.objects.get(id=request.user.pk)

    form_profile = UpdateMemberProfile(instance = profile)
    form_user = CreateUserForm(instance = user_update)
    form_nopass = UpdateJustBasicFilesUser(instance = user_update_nopass)

    if request.method == 'POST':
        print("Aqui entro al post")
        form_profile = UpdateMemberProfile(request.POST,request.FILES, instance = profile)
        form_user = CreateUserForm(request.POST, instance = user_update)
        form_nopass = UpdateJustBasicFilesUser(request.POST,instance=user_update_nopass)
        print("Si soy válido en POST")

        # |=| Validamos el correo  si es      |=|
        # |=| que este existe.                |=|
        emailtest = request.POST['membEmail']
        # |=| si este que existe pregunta.        |=|
        if member.objects.filter(membEmail=emailtest).exists():
            # |=| Pregunta si el correo actual          |=|
            # |=| es igual al correo a actualizar       |=|
            if request.user.member.membEmail == emailtest:
                # |=| Si es igual los actualiza       |=|
                memberUpdateMethod(request,form_profile,form_nopass,form_user,user_update)
                print('Si jalo')
            else:
                # |=| Si no es igual no los actualiza |=|
                messages.warning(request,"El correo que desea actualizar ya existe.")     
        else:
            # |=| Si que este no existe, lo actualiza    |=|
            memberUpdateMethod(request,form_profile,form_nopass,form_user,user_update)
        return redirect('profile')
    context = {
        'form_profile': form_profile,
        'form_user':form_user
    }
    return render(request,'member/profile.html',context)

# |=========================================|
# |=====|   ACTUALIZACIÓN DE DATOS    |=====|
# |=========================================|
# |=| Se muestran los avistadores  que se |=|
# |=| han logeado en la página.           |=|
# |=========================================|
def memberUpdateMethod(request,form_profile,form_nopass,form_user,user_update):
    # |=| Validación de formulario 1      |=|
    if form_profile.is_valid():
        print("Si soy válido x2")
        form_profile.save()
        text = "Datos actualizados correctamente."
        # |=| Validación de formulario 2      |=|
        if form_nopass.is_valid():
            print("Si soy válido en sin pass")
            form_nopass.save()
            # |=| Validación de formulario 3      |=|
            if form_user.is_valid():
                print("Si soy válido en formulario")
                password1 = form_user.cleaned_data.get('password1')
                password2 = form_user.cleaned_data.get('password2')

                if password1 == password2:
                    usernameIn = request.user
                    passwordIn = password1
                    user_update.set_password(password1)

                    form_user.save()
                    # |=| Logeo automático            |=|
                    login(request, usernameIn, passwordIn)
                    print("Si guarde datos 1")   
        messages.success(request,text)
    else:
        print("No fununcie")


# |==========================================|
# |=====|      Error 404 Not Found     |=====|
# |==========================================|
# |=|   Proceso de Ckech in de trabajador. |=|
# |==========================================|
def error404(request, exception):
    return render(request, 'errors/404.html')