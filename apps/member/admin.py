from django.contrib import admin

# Register your models here.
from .models import member

# |-----| Visualización de los campos de la tabla de trabajadores |-----| 
@admin.register(member)
class memberList(admin.ModelAdmin):
    list_display = ["membUser","membPhone"]