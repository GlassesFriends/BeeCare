# |=============================================================|
# |===============|         BIBLIOTECAS         |===============|
# |=============================================================|

# |=========================================|
# |=====|       BIBLIOTECAS BASE      |=====|
# |=========================================|
from django.db import models

# |==============================================|
# |=====|       BIBLIOTECAS ADICIONALES     |====|
# |==============================================|
from statistics import mode
from django.db import models
from pathlib import Path

# Create your models here.

# |=========================================|
# |========|     MODELO CATEGORY    |=======|
# |=========================================|
class Category(models.Model):
    categoryTitle = models.CharField(max_length=255)

    def __str__(self):
        return self.categoryTitle

# |=========================================|
# |========|     MODELO BEEPOST     |=======|
# |=========================================|
class BeePost(models.Model):
    bPostCategory = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    bPostCoverImage = models.ImageField(upload_to='BeePost/',blank=True)
    bPostTitle = models.CharField(max_length=255)
    bPostSlug = models.SlugField(max_length=255)
    bPostIntro = models.TextField()
    bPostBody = models.TextField()
    bPostCreated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-bPostCreated_at', )

    def __str__(self):
        return self.bPostTitle

# |=========================================|
# |========|     MODELO COMMENT     |=======|
# |=========================================|
class Comment(models.Model):
    commentBeepost = models.ForeignKey(BeePost, related_name='comments', on_delete=models.CASCADE)
    commentName = models.CharField(max_length=255)
    commentEmail = models.EmailField(max_length=255)
    commentText = models.TextField()
    commentCreated_at = models.DateTimeField(auto_now_add=True)