# |=============================================================|
# |===============|         BIBLIOTECAS         |===============|
# |=============================================================|

# |=========================================|
# |=====|       BIBLIOTECAS BASE      |=====|
# |=========================================|

from django.db import models
# |=========================================|
# |=====|       BIBLIOTECAS BASE      |=====|
# |=========================================|


# |=========================================|
# |=====|     BIBLILIOTECAS EXTRAS    |=====|
# |=========================================|

from pathlib import Path
from apps.member.models import member

# |=============================================================|
# |===============|           MODELOS           |===============|
# |=============================================================|

# |=========================================|
# |========|     MODELO FAMILY      |=======|
# |=========================================|

class family (models.Model):
    familyName = models.CharField(max_length=80)
    def __str__(self):
        return self.familyName

# |=========================================|
# |========|    MODELO SUBFAMILY    |=======|
# |=========================================|

class subfamily (models.Model):
    subfamilyName = models.CharField(max_length=80)
    subfamilyFamily = models.ForeignKey(family,on_delete=models.CASCADE)
    def __str__(self):
        return self.subfamilyName

# |=========================================|
# |========|     MODELO GENDER      |=======|
# |=========================================|

class gender (models.Model):
    genderName = models.CharField(max_length=80)
    def __str__(self):
        return self.genderName

# |=========================================|
# |========|     MODELO SPECIES     |=======|
# |=========================================|
class species (models.Model):
    speciesName = models.CharField(max_length=80)
    def __str__(self):
        return self.speciesName

# |=========================================|
# |========|  MODELO BEE (species,  |=======|
# |=========================================|
# |========|   subfamily,family)    |=======|
# |=========================================|

class bee (models.Model):
    beeName = models.CharField(max_length=64)
    beeSpecies = models.ForeignKey(species,on_delete=models.CASCADE)
    beeSubfamily = models.ForeignKey(subfamily,on_delete=models.CASCADE)
    beeGender = models.ForeignKey(gender,on_delete=models.CASCADE)
    def __str__(self):
        return self.beeName
    
# |=| Método para guardar imagenes de los |=|
# |=| avistamientos realizados por los    |=|
# |=| miembros                            |=|

def get_img_sighting(instance,filename):
    extension = Path(filename).suffix
    return 'Sightings/sighting_%s/sight.%s' % (instance.sighMember,extension)

# |=========================================|
# |========| MODELO SIGHTING (memb) |=======|
# |=========================================|

class sighting (models.Model):
    sighLat = models.DecimalField(max_digits=32,decimal_places=16, blank=True,null=True)
    sighLng = models.DecimalField(max_digits=32,decimal_places=16, blank=True, null=True)
    sighPicture = models.ImageField(upload_to=get_img_sighting,blank=True)
    sighComment = models.CharField(max_length=1024)
    sighDate = models.DateTimeField(auto_now_add=True,auto_now=False)
    sighApproved = models.BooleanField(default=False)
    sighBee = models.ForeignKey(bee,on_delete=models.CASCADE)
    sighMember = models.ForeignKey(member,on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.sighDate,self.sighApproved)