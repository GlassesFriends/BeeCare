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
from apps.member.models import member

# Create your models here.

# |=========================================|
# |========|     MODELO CATEGORY    |=======|
# |=========================================|
class category(models.Model):
    categoryTitle = models.CharField(max_length=255)

    def __str__(self):
        return self.categoryTitle

# |=========================================|
# |========|     MODELO BEEPOST     |=======|
# |=========================================|
class beePost(models.Model):
    bPostCategory = models.ForeignKey(category, related_name='posts', on_delete=models.CASCADE)
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
class comment(models.Model):
    commentBeepost = models.ForeignKey(beePost, related_name='comments', on_delete=models.CASCADE)
    commentMember = models.ForeignKey(member, related_name='email', on_delete=models.CASCADE)
    commentText = models.TextField()
    commentCreated_at = models.DateTimeField(auto_now_add=True)