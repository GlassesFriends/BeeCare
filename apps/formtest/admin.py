# |=============================================================|
# |===============|         BIBLIOTECAS         |===============|
# |=============================================================|
# |=========================================|
# |=====|       BIBLIOTECAS BASE      |=====|
# |=========================================|
from django.contrib import admin
# |=========================================|
# |=====|     REFERENCIAS A MODELOS   |=====|
# |=========================================|
from apps.formtest.models import testform,question,answer,answerusr

# Register your models here.
# |-----|    Visualización de los campos de la tabla testform    |-----| 
@admin.register(testform)
class testformList(admin.ModelAdmin):
    list_display = ["id","testName"]
# |-----|    Visualización de los campos de la tabla question    |-----| 
@admin.register(question)
class questionList(admin.ModelAdmin):
    list_display = ["id","questionTittle"]
# |-----|    Visualización de los campos de la tabla answer      |-----| 
@admin.register(answer)
class answerList(admin.ModelAdmin):
    list_display = ["id","answerDescription"]
# |-----|    Visualización de los campos de la tabla answerusr   |-----| 
@admin.register(answerusr)
class answerusrList(admin.ModelAdmin):
    list_display = ["id","answerusrToquestion","answerusrMember"]
