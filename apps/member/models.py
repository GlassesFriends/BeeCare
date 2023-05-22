# |=============================================================|
# |===============|         BIBLIOTECAS         |===============|
# |=============================================================|

# |=========================================|
# |=====|       BIBLIOTECAS BASE      |=====|
# |=========================================|

from django.db import models
from django.contrib.auth.models import User

# |=========================================|
# |=====|   BIBLIOTECAS ADICIONALES   |=====|
# |=========================================|
import pathlib

# |=| Generación de números aleatorios    |=|
# |=| enteros.                            |=|
from random import randint
# |=| Atributo de color en modelos.       |=|
from colorfield.fields import ColorField

# |=============================================================|
# |===============|     MÉTODOS GLOBLAES        |===============|
# |=============================================================|

# |=| Método para localizar el path de la |=|
# |=| fotografía del trabajador.          |=|
def get_memb_image_filepath(instance, filename):
    extension  = pathlib.Path(filename).suffix
    return 'memb/memb_%s/profile_picture.%s' % (instance.membEmail, extension)

# |=| Método que asigna una fotografía al |=|
# |=| trabajador registrado.              |=|
# |=| Para el caso de esta app, el núm    |=|
# |=| maximo se debe considerar respecto  |=|
# |=| a la cantidad de opciones de foto   |=|
# |=| en la carpeta "static/memb/".     |=|
def get_default_memb_image():
    return "memb/memb_memb_image" + str(randint(0, 5)) + ".png"

# |=============================================================|
# |===============|           MODELOS           |===============|
# |=============================================================|

# |=========================================|
# |=====|  MODELO TRABAJADOR (memb) |=====|
# |=========================================|
class member(models.Model):
    # |=| Se trata del nombre del miembro.      |=|
    membFirstName = models.CharField(
        max_length=35, verbose_name=u"Nombres", null=False)
    
    # |=| Se trata del apellido del miembro.    |=|
    membLastName = models.CharField(
        max_length=35, verbose_name=u"Apellidos", null=False)
    
    # |=| Fecha de nacimiento del trabajador.   |=|
    membDateBirth = models.DateField(
        verbose_name=u"Fecha de nacimiento", null=True)
    
    # |=| Se trata del apellido del miembro.    |=|
    membPhone = models.CharField(
        max_length=20, verbose_name=u"Número de teléfono", null=True)
    
    # |=| Fotografía del portada del miembro.   |=|
    membCoverPicture = models.ImageField(
        max_length=255,
        upload_to=get_memb_image_filepath,
        blank=True, default=get_default_memb_image,
        verbose_name=u"Foto de Portada")
    
    # |=| Fotografía del miembro.               |=|
    # |=| Se le asinará una por defecto al      |=|
    # |=| registrase.                           |=|
    membProfilePicture = models.ImageField(
        max_length=255,
        upload_to=get_memb_image_filepath,
        blank=True, default=get_default_memb_image,
        verbose_name=u"Foto de perfil")
    
    # |=| Registro de la fecha de registro del  |=|
    # |=| trabajador.                           |=|
    membregdate = models.DateField(auto_now_add=True)
    
    # |=| "Bandera" para saber si el trabajador |=|
    # |=| es activo o no.                       |=|
    membIsActive = models.BooleanField(
        default=False, verbose_name=u"Usuario activo")
    
    # |=| Este será considerado como su nombre  |=|
    # |=| de usuario (username).                |=|
    # |=| Este se tomará del model de django.   |=|
    membEmail = models.EmailField(
        max_length=64, verbose_name=u"Correo electrónico", unique=True)
    
    # |=| Relación uno a uno con el modelo user |=|
    membUser = models.OneToOneField(User, null=False, on_delete=models.CASCADE)

    # |=| --------------------------------------------------------------------- |=|
    # |=| MUY IMPORTANTE PARA LA INTEGRIDAD,  MUY IMPORTANTE PARA LA INTEGRIDAD |=|
    # |=| --------------------------------------------------------------------- |=|
    
    # |=| Asignación de "nombre" de objeto.     |=|
    def __str__(self):
        return "%s %s" % (self.membLastName, self.membFirstName)
    # |=| --------------------------------------------------------------------- |=|
    # |=| ----------------------| EJEMPLO DE IMPRESION |----------------------- |=|
    # |=| --------------------------------------------------------------------- |=|
    # |=| ------------| {{member}} = González Álvaro               |----------- |=|
    # |=| ------------| {{member.membLastName}} != González Álvaro |----------- |=|
    # |=| --------------------------------------------------------------------- |=|
    
    
    # |=| --------------------------------------------------------------------- |=|
    # |=| MUY IMPORTANTE PARA LA INTEGRIDAD,  MUY IMPORTANTE PARA LA INTEGRIDAD |=|
    # |=| --------------------------------------------------------------------- |=|

    # |=| Permite una ubicación rápida de las   |=|
    # |=| instancias creadas de este model.     |=|
    # |=| BASADO EN EL APELLIDO DEL MIEMBRO     |=|
    class Meta:
        ordering = ['membLastName']