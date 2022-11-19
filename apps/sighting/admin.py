from django.contrib import admin
from apps.sighting.models import family,subfamily,gender,species,bee,sighting
# Register your models here.

# |-----|    Visualización de los campos de la tabla family    |-----| 
@admin.register(family)
class FamilyAdmin(admin.ModelAdmin):
    list_display = ["id"]

# |-----|   Visualización de los campos de la tabla subfamily  |-----| 
@admin.register(subfamily)
class SubfamilyAdmin(admin.ModelAdmin):
    list_display = ["id"]

# |-----|    Visualización de los campos de la tabla gender    |-----| 
@admin.register(gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ["id"]

# |-----|    Visualización de los campos de la tabla species   |-----| 
@admin.register(species)
class SpeciesAdmin(admin.ModelAdmin):
    list_display = ["id"]

# |-----|      Visualización de los campos de la tabla bee     |-----| 
@admin.register(bee)
class BeeAdmin(admin.ModelAdmin):
    list_display = ["id","beeName"]

# |-----|   Visualización de los campos de la tabla sighting   |-----| 
@admin.register(sighting)
class SightingAdmin(admin.ModelAdmin):
    list_display = ["id"]
