# |=============================================================|
# |===============|         BIBLIOTECAS         |===============|
# |=============================================================|

# |=========================================|
# |=====|       BIBLIOTECAS BASE      |=====|
# |=========================================|
from django.contrib import admin

from .models import category, beePost, comment

# Register your models here.
@admin.register(category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "categoryTitle"]
    
@admin.register(beePost)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "bPostTitle", "bPostSlug", "bPostCreated_at"]

@admin.register(comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["id", "commentMember", "commentCreated_at"]