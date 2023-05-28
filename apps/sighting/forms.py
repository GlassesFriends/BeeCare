# |=============================================================|
# |===============|         BIBLIOTECAS         |===============|
# |=============================================================|

# |=========================================|
# |=====|       BIBLIOTECAS BASE      |=====|
# |=========================================|
from django import forms

# |=========================================|
# |=====|     REFERENCIAS A MODELOS   |=====|
# |=========================================|
from .models import subfamily,family,gender,species,bee,sighting,field


# |=============================================================|
# |===============|       FORMULARIOS           |===============|
# |=============================================================|

# |=========================================|
# |=====| FORMULARIO DE SUBFAMILYFORM |=====|
# |=========================================|
# |=| Se da formato a cada uno de los     |=|
# |=| campos que se utilizarán.           |=|
# |=========================================|

class SubfamilyForm(forms.ModelForm):
    class Meta:
        model = subfamily
        fields = [
            "subfamilyName",
        ]

# |=========================================|
# |=====|   FORMULARIO DE FAMILYFORM  |=====|
# |=========================================|
# |=| Se da formato a cada uno de los     |=|
# |=| campos que se utilizarán.           |=|
# |=========================================|

class FamilyForm(forms.ModelForm):
    class Meta:
        model = family
        fields = [
            "familyName",
        ]

# |=========================================|
# |=====|   FORMULARIO DE GENDERFORM  |=====|
# |=========================================|
# |=| Se da formato a cada uno de los     |=|
# |=| campos que se utilizarán.           |=|
# |=========================================|

class GenderForm(forms.ModelForm):
    class Meta:
        model = gender
        fields = [
            "genderName",
        ]

# |=========================================|
# |=====|  FORMULARIO DE SPECIESFORM  |=====|
# |=========================================|
# |=| Se da formato a cada uno de los     |=|
# |=| campos que se utilizarán.           |=|
# |=========================================|

class SpeciesForm(forms.ModelForm):
    class Meta:
        model = species
        fields = [
            "speciesName",
        ]

# |=========================================|
# |=====|    FORMULARIO DE BEEFORM    |=====|
# |=========================================|
# |=| Se da formato a cada uno de los     |=|
# |=| campos que se utilizarán.           |=|
# |=========================================|

class BeeForm(forms.ModelForm):
    class Meta:
        model = bee
        fields = [
            "beeName",
        ]

# |=========================================|
# |=====|  FORMULARIO DE SIGHTINGFORM |=====|
# |=========================================|
# |=| Se da formato a cada uno de los     |=|
# |=| campos que se utilizarán.           |=|
# |=========================================|

class SightingForm(forms.ModelForm):
    class Meta:
        model = sighting
        fields = [
            "sighLat",
            "sighLng",
            "sighPicture",
            "sighComment",
        ]

# |=========================================|
# |=====|  FORMULARIO DE FIELDFORM    |=====|
# |=========================================|
# |=| Se da formato a cada uno de los     |=|
# |=| campos que se utilizarán.           |=|
# |=========================================|

class FieldForm(forms.ModelForm):
    class Meta:
        model = field
        fields = [
            "fieldsting",
            "fieldnative",
        ]