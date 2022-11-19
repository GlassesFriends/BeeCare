# |=============================================================|
# |===============|         BIBLIOTECAS         |===============|
# |=============================================================|

# |=========================================|
# |=====|       BIBLIOTECAS BASE      |=====|
# |=========================================|
from django.http import HttpResponse
from django.shortcuts import redirect

# |=========================================|
# |=====|   BIBLIOTECAS ADICIONALES   |=====|
# |=========================================|
from django.contrib import messages

# |=============================================================|
# |===============|    USUARIO AUTENTIFICADO    |===============|
# |=============================================================|
# |=|  Se trata de la validación para corroborár que el       |=|
# |=|  usuario que esté intentando ingresar esté logueado.    |=|
# |=============================================================|
def user_auth(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, *kwargs)
        else:
            return redirect('home') 
    return wrapper_func

# |=============================================================|
# |===============|      USUARIO PERMITIDO      |===============|
# |=============================================================|
# |=|  Decorador que permite revisar si el usuario esta       |=|
# |=|  registrado en el grupo que le permita ingresar a dicho |=|
# |=|  view al que intente ingresar.                          |=|
# |=============================================================|
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            groups = None
            if request.user.groups.exists():
                groups = request.user.groups.all()[0].name
                print(group)
            else:
                return redirect('home')
            
            for group in groups:
                if group in allowed_roles:
                    return view_func(request, *args, **kwargs)
                else:
                    return redirect('home')
        return wrapper_func
    return decorator