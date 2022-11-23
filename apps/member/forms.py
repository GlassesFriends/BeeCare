# |=============================================================|
# |===============|         BIBLIOTECAS         |===============|
# |=============================================================|

# |=========================================|
# |=====|       BIBLIOTECAS BASE      |=====|
# |=========================================|
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# |=========================================|
# |=====|   BIBLIOTECAS ADICIONALES   |=====|
# |=========================================|
from .models import member

# |=============================================================|
# |===============|       FORMULARIOS           |===============|
# |=============================================================|

# |=========================================|
# |=====|   FORMULARIO DE REGISTRO    |=====|
# |=========================================|
# |=| Se da formato a cada uno de los     |=|
# |=| campos que se utilizarán.           |=|
# |=========================================|
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'password1', 'password2']

# |=========================================|
# |=====|    FORMULARIO DE MEMBER     |=====|
# |=========================================|
# |=| Se da formato a cada uno de los     |=|
# |=| campos que se utilizarán.           |=|
# |=========================================|

class UpdateMemberProfile(ModelForm):
	class Meta:
		model = member
		fields = ['membFirstName','membLastName','membDateBirth','membPhone','membProfilePicture','membEmail']

# |=========================================|
# |=====|    FORMULARIO DE UserUBF    |=====|
# |=========================================|
# |=| Se da formato a cada uno de los     |=|
# |=| campos que se utilizarán.           |=|
# |=========================================|
class UpdateJustBasicFilesUser(ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username']