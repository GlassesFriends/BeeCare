# |=============================================================|
# |===============|         BIBLIOTECAS         |===============|
# |=============================================================|

# |=========================================|
# |=====|       BIBLIOTECAS BASE      |=====|
# |=========================================|
from django.db import models

# |=========================================|
# |=====|     BIBLILIOTECAS EXTRAS    |=====|
# |=========================================|

from apps.member.models import member

# Create your models here.

# |=============================|
# |========== testform =========|
# |=============================|

class testform(models.Model):
    testName = models.CharField(max_length=250)
    def __str__(self):
        return self.testName
    
# |=============================|
# |========== question =========|
# |=============================|
class question(models.Model):
    questionTittle = models.CharField(max_length=200)
    questionName = models.CharField(max_length=250)
    questionTestform = models.ForeignKey(testform,on_delete=models.CASCADE) 
    def __str__(self):
        return self.questionTittle

# |=============================|
# |=========== answer ==========|
# |=============================|
class answer(models.Model):
    answerDescription = models.CharField(max_length=250)
    answerRight = models.BooleanField(default=True)
    answerQuestion = models.ForeignKey(question,on_delete=models.CASCADE)
    def __str__(self):
        return self.answerDescription

# |=============================|
# |========= answerusr =========|
# |=============================|
class answerusr(models.Model):
    answerusrToquestion = models.CharField(max_length=10)
    answerusrDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    answerusrQuestion = models.ForeignKey(question,on_delete=models.CASCADE)
    answerusrMember = models.ForeignKey(member, on_delete=models.CASCADE)
    def __str__(self):
        return self.answerusrToquestion
