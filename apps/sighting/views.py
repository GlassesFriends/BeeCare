# |=============================================================|
# |===============|         BIBLIOTECAS         |===============|
# |=============================================================|

# |=========================================|
# |=====|       BIBLIOTECAS BASE      |=====|
# |=========================================|
from django.shortcuts import render,redirect
from django.http import JsonResponse
# |=========================================|
# |=====|       BIBLIOTECAS BASE      |=====|
# |=========================================|
from django.contrib import messages

# |=========================================|
# |=====|     BIBLILIOTECAS EXTRAS    |=====|
# |=========================================|
from abc import abstractmethod

# |=========================================|
# |=====|     REFERENCIAS A MODELOS   |=====|
# |=========================================|
from .models import subfamily,family,gender,species,bee,sighting,field,beefield
from apps.member.decorators import user_auth

# |=========================================|
# |=====|  REFERENCIAS A FORMULARIOS  |=====|
# |=========================================|
from .forms import SubfamilyForm,FamilyForm,GenderForm,SpeciesForm,BeeForm,SightingForm,FieldForm

# |=============================================================|
# |===============|      COMIENZAN VISTAS       |===============|
# |=============================================================|

# |=| Método para ingresar avistamiento |=|

@user_auth
def sightingRegister(request):
    # |========================================|
    # |=| Almacenamiento de valores de la BD |=|
    field_family = family.objects.all().order_by('familyName')
    field_subfamily = subfamily.objects.all().order_by('subfamilyName')
    field_gender = gender.objects.all().order_by('genderName')
    field_species = species.objects.all().order_by('speciesName')
    field_bee = bee.objects.all().order_by('beeName')
    field_field = field.objects.all().order_by('fieldsting')

    # |=| Formularios a utilizar             |=|
    form1_family = FamilyForm()
    form2_subfamily = SubfamilyForm()
    form3_gender = GenderForm()
    form4_species = SpeciesForm()
    form5_bee = BeeForm()
    form6_sighting = SightingForm()
    form7_field = FieldForm()

    # |=| Condicional de igualdad del método |=|
    # |=| POST, asignación de request para   |=|
    # |=| los formularios.                   |=|
    # |=|NOTA:FILES para imagenes cloudinary |=|
    # |========================================|

    if request.method == 'POST':
        # |========================================|
        form1_family = FamilyForm(request.POST)
        form2_subfamily = SubfamilyForm(request.POST)
        form3_gender = GenderForm(request.POST)
        form4_species = SpeciesForm(request.POST)
        form5_bee = BeeForm(request.POST)
        form6_sighting = SightingForm(request.POST,request.FILES)
        form7_field = FieldForm(request.POST)

        error = "Hubo un error al guardar la información."
        print('Aquí entro a post')

        # |========================================|
        # |=| Válidación de formulario de family |=|
        # |========================================|    
        if form1_family.is_valid():
            # |===========================================|
            familyName = form1_family.cleaned_data.get('familyName')
            # |===========================================| 
            # |=|     get_or_created para family        |=|
            # |===========================================| 
            fam,created1 = family.objects.get_or_create(
            familyName = familyName
            )

            print('Si cargo chido 1')
            # |=|   Guardado de datos para family       |=|
            fam.save()

            # |===========================================|
            # |=| Válidación de formulario de subfamily |=|
            # |===========================================|
            if form2_subfamily.is_valid():
                # |========================================|
                subfamilyName = form2_subfamily.cleaned_data.get('subfamilyName')
                # |==========================================| 
                # |=|    get_or_created para subfamily     |=|
                # |==========================================| 
                subfam,created2 = subfamily.objects.get_or_create(
                subfamilyName = subfamilyName,
                subfamilyFamily = fam
                )

                print('Si cargo chido 2')
                # |=|  Guardado de datos para subfamily  |=|
                subfam.save()

                # |========================================|
                # |=| Válidación de formulario de gender |=|
                # |========================================|
                if form3_gender.is_valid():
                    genderName = form3_gender.cleaned_data.get('genderName')
                    # |==========================================|
                    # |=|     get_or_created para gender       |=|
                    # |==========================================|              
                    gen,created3 = gender.objects.get_or_create(
                    genderName = genderName,
                    )

                    print('Si cargo chido 3')
                    # |=|  Guardado de datos para gender       |=|
                    gen.save()

                    # |==========================================|
                    # |=| Válidación de formulario de species  |=|
                    # |==========================================|
                    if form4_species.is_valid():
                        speciesName = form4_species.cleaned_data.get('speciesName')
                        # |==========================================|        
                        # |=|      get_or_created para species     |=|
                        # |==========================================|      
                        specie,created4 = species.objects.get_or_create(
                        speciesName = speciesName,
                        )
                        print('Si cargo chido 4')
                        # |=|    Guardado de datos para species    |=|
                        specie.save()

                        # |==========================================|
                        # |=|   Válidación de formulario de bee    |=|
                        # |==========================================|
                        if form5_bee.is_valid():
                            beeName = form5_bee.cleaned_data.get('beeName')
                            # |===========================================| 
                            # |=|       get_or_created para bee         |=|
                            # |===========================================| 
                            beee,created5 = bee.objects.get_or_create(
                                beeName = beeName,
                                beeSpecies = specie,
                                beeSubfamily = subfam,
                                beeGender = gen
                            )
                            print('Si cargo chido 5')
                            # |=|      Guardado de datos para bee      |=|
                            beee.save()
                            print('REgistró abeja')

                            # |==========================================|
                            # |=| Válidación de formulario de sighting |=|
                            # |==========================================|
                            if form6_sighting.is_valid():
                                sighLat = form6_sighting.cleaned_data.get('sighLat')
                                sighLng = form6_sighting.cleaned_data.get('sighLng')
                                sighPicture = form6_sighting.cleaned_data.get('sighPicture')
                                sighComment = form6_sighting.cleaned_data.get('sighComment')
                                # |==========================================| 
                                # |=|      get_or_created para sighting    |=|
                                # |==========================================| 
                                sigh = sighting.objects.create(
                                sighLat = sighLat,
                                sighLng = sighLng,
                                sighPicture = sighPicture,
                                sighComment = sighComment,
                                sighApproved = False,
                                sighBee = beee,
                                sighMember = request.user.member,  
                                ) 
                                print('Si cargo chido 6')
                                # |=|     Guardado de datos para sighting  |=|
                                sigh.save()

                                # |==========================================|
                                # |=|          Validación de field         |=|
                                # |==========================================|
                                if form7_field.is_valid():
                                    fieldsting = form7_field.cleaned_data.get('fieldsting')
                                    fieldnative = form7_field.cleaned_data.get('fieldnative')
                                    # |==========================================| 
                                    # |=|      get_or_created para sighting    |=|
                                    # |==========================================|
                                    fieldd,created7 = field.objects.get_or_create(
                                    fieldsting = fieldsting,
                                    fieldnative = fieldnative,
                                    )           
                                    print('Si cargo chido 7')
                                    fieldd.save()

                                    beefieldd = beefield.objects.create(
                                        beefieldBee = beee,
                                        beefieldField = fieldd,
                                    )
                                    beefieldd.save()
                                    print('Si cargo chido 8')

                                messages.success(request,"Avistamiento registrado exitosamente.")
                            else:
                                print("No jalo el avistamiento")
                                messages.error(request,error)           
            return redirect ('sighting-reg')
        else:
            print('jajaja no fununcie')
            messages.error(request,error)
    context = { 

        'familys':field_family,
        'subfamilys':field_subfamily,
        'genders':field_gender,
        'species':field_species,
        'bees':field_bee,
        'avist':'active',
    }
    return render(request,'sighting/sighting-reg.html', context)


# |=========================================|
# |===== Main patrón template method =======|
# |=========================================|
# |=| Método para ingresar avistamiento   |=|
def sightingMap(request):
    mySightings = sighting.objects.all().filter(sighApproved=True)

    # |=|   Llamadas a instancias de la   |=|
    # |=|       clase AbstractClass       |=|
    r1 = ConcreteClass1.getRequest(AbstractClass())
    r2 = ConcreteClass2.getRequest(AbstractClass())

    context = { 
        'sightings': mySightings,
        'avist':'active',
        'Aproved':r1,
        'NoAproved':r2,
    }
    
    return render(request,'sighting/sighting-map.html', context)


# |=|    Clase con método abstracto    |=|
# |=|        y método template         |=|
class AbstractClass():
    # |=| Método template    |=| 
    def template_method(self):
        self.getRequest()
    # |=| Método abstracto   |=| 
    @abstractmethod
    def getRequest(self):
        pass

# |=|         Clase concreta 1         |=| 
class ConcreteClass1(AbstractClass):
    def getRequest(self):
        retorno = []
        for z in sighting.objects.all().filter(sighApproved=True):
            elemento = [z.id]
            retorno.append(elemento)
        retorno =len(retorno)
        return retorno

# |=|         Clase concreta 2         |=| 
class ConcreteClass2(AbstractClass):
    def getRequest(self):
        retorno = []
        for z in sighting.objects.all().filter(sighApproved=False):
            elemento = [z.id]
            retorno.append(elemento)
        retorno =len(retorno)
        return retorno



@user_auth
def sightingMapOwn(request):
    mySightings = sighting.objects.all().filter(
        sighMember=request.user.member
        ).order_by('sighApproved')[:6]
        
    context = { 
        'sightings': mySightings,
        'avist':'active',
    }
    return render(request,'sighting/sightings.html', context)

# |=| Método para Json de sightings |=|
def get_Sighting(request):
    sightings = list(sighting.objects.values().filter(sighApproved=True))

    if(len(sightings) > 0):
        data = {'message': "Success",'sighting':sightings}
    else:
        data = {'message': "No se encontro"}
    return JsonResponse(data)

# |=| Método para Json de sightings |=|
def get_Sighting_Personal(request):
    sightings = list(sighting.objects.values().filter(sighMember=request.user.member))

    if(len(sightings) > 0):
        data = {
            'message': "Success",
            'sighting':sightings,
            }
    else:
        data = {
            'message': "No se encontro",
            }
    return JsonResponse(data)

# |=| Método para Json de sightings |=|
def get_Sighting_General(request):
    sightings = list(sighting.objects.values().filter(sighApproved=True))

    if(len(sightings) > 0):
        data = {
            'message': "Success",
            'sighting':sightings,
            }
    else:
        data = {
            'message': "No se encontro",
            }
    return JsonResponse(data)

# |=| Método para Json de bees      |=|
def get_Bee(request):
    bees = list(bee.objects.values())

    if(len(bees) > 0):
        data = {'message': "Success",'bee':bees}
    else:
        data = {'message': "No se encontro"}
    return JsonResponse(data)

# |=|  Método para Json de familys  |=|
def get_Family(request):
    familys = list(family.objects.values())

    if(len(familys) > 0):
        data = {'message': "Success",'family':familys}
    else:
        data = {'message': "No se encontro"}
    return JsonResponse(data)

# |=|Método para Json de subfamilys |=|
def get_Subfamily(request):
    subfamilys = list(subfamily.objects.values())

    if(len(subfamilys) > 0):
        data = {'message': "Success",'subfamily':subfamilys}
    else:
        data = {'message': "No se encontro"}
    return JsonResponse(data)


# |=| Avistamientos aprobados       |=|
def get_Sighting_map(request):
    sightings = list(sighting.objects.values().filter(sighMember=request.user.member))

    if(len(sightings) > 0):
        data = {'message': "Success",'sighting':sightings}
    else:
        data = {'message': "No se encontro"}
    return JsonResponse(data)


def get_sightings(request,pk):
    sightings = sighting.objects.filter(pk=pk)
    context =  {
        'message': "Success",
        'avistamiento':sightings,
        'avist':'active',
        }
    return render(request,'sighting/avistamiento.html',context)

