from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Mensaje(models.Model):
    cuerpo = RichTextField()
    destinatario = models.CharField(max_length=20)
    autor = models.CharField(max_length=20)
    
    def __str__(self):
        return f'Destinatario: {self.destinatario} - Cuerpo: {self.cuerpo} - Autor: {self.autor}'