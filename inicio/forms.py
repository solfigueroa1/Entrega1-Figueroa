from django import forms

class CrearFutbolistaFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    fecha_nacimiento = forms.DateField(required=False)
    