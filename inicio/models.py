from django.db import models

# Create your models here.

class Futbolista(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField(null=True)
    
    