# |=============================================================|
# |===============|         BIBLIOTECAS         |===============|
# |=============================================================|

# |=========================================|
# |=====|       BIBLIOTECAS BASE      |=====|
# |=========================================|
from django.contrib import admin

from .models import Category, BeePost, Comment

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "categoryTitle"]
    
@admin.register(BeePost)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "bPostTitle", "bPostSlug", "bPostCreated_at"]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["id", "commentName", "commentEmail", "commentCreated_at"]