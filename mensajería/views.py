from django.shortcuts import render,redirect
from mensajería.forms import CrearMensajeFormulario
from mensajería.models import Mensaje
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def crear_mensaje(request):
    
    if request.method == 'POST':
        formulario = CrearMensajeFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            info = formulario.cleaned_data
            mensaje = Mensaje(destinatario=info['destinatario'], cuerpo=info['cuerpo'], autor=info['autor'])
            mensaje.save()
            return redirect('mensajería:mensajes')
        else:
            return render(request, 'mensajería/crear_mensaje.html', {'formulario' : formulario})
    
    formulario = CrearMensajeFormulario()
    return render(request, 'mensajería/crear_mensaje.html', {'formulario': formulario})

@login_required
def mensajes(request):
    mensajes = Mensaje.objects.all()
    return render(request, 'mensajería/mensajes.html', {'mensajes': mensajes})
