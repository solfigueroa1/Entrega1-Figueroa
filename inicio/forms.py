from django import forms
from ckeditor.fields import RichTextFormField

class CrearFutbolistaFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    fecha_nacimiento = forms.DateField(required=False)
    descripcion = RichTextFormField()
    autor = forms.CharField(required=False)
    imagen = forms.ImageField(required=False)
    
class BuscarFutbolistaFormulario(forms.Form):
    nombre = forms.CharField(max_length=40, required=False)
    
class CrearHockistaFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    fecha_nacimiento = forms.DateField(required=False)
    
class CrearVoleibolistaFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    fecha_nacimiento = forms.DateField(required=False)
    
    
    
    