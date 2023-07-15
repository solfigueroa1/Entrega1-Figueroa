from django import forms
from ckeditor.fields import RichTextFormField


class CrearMensajeFormulario(forms.Form):
    cuerpo = RichTextFormField()
    destinatario = forms.CharField(max_length=20)
    autor = forms.CharField(max_length=20)
    
