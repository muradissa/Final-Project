from django.db import models
import string 
import random

def generate_unique_string_code():
    length = 8
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Wall.objects.filter(code=code).count() == 0:
            break
    return code


# Create your models here.
class Anchor(models.Model):
    code = models.IntegerField(null=False,default=0,unique=True)
    anchor_is_help = models.BooleanField(null=False , default=False)
    x = models.IntegerField(null=False,default=0)
    y = models.IntegerField(null=False,default=0)
    
class Wall(models.Model):
    code = models.CharField(max_length=8 ,default=generate_unique_string_code,unique=True)
    host = models.CharField(max_length=50 ,unique=True)
    
    height = models.IntegerField(null=False , default = 20)
    width = models.IntegerField(null=False , default = 50)
    angle = models.IntegerField(null=False , default = 90)
    number_of_anchors = models.IntegerField(null=False , default=100)
    anchorsInRow = models.IntegerField(null=False , default=0)
    anchorsInCol = models.IntegerField(null=False , default=0)
    bloop = models.BooleanField(null=False , default=False)

    v = models.FloatField(null=False , default = 0.1)
    c = models.IntegerField(null=False , default = 1)  
    e = models.IntegerField(null=False , default = 30)  
    i = models.IntegerField(null=False , default = 104)
    

class Parameters(models.Model):
    optimizationType = models.IntegerField(null=False,default=0)
    strategyType = models.IntegerField(null=False,default=0)
    dimensionalType =models.IntegerField(null=False,default=0)

