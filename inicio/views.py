from django.shortcuts import render,redirect
from inicio.forms import CrearFutbolistaFormulario, CrearVoleibolistaFormulario, CrearHockistaFormulario, BuscarFutbolistaFormulario
from inicio.models import Futbolista, Hockista, Voleibolista
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def inicio(request):
    return render(request, 'inicio/inicio.html')

def about(request):
    return render(request,'inicio/about.html')


@login_required
def crear_futbolista(request):
    mensaje = ''
    
    if request.method == 'POST':
        formulario = CrearFutbolistaFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            info = formulario.cleaned_data
            futbolista = Futbolista(nombre=info['nombre'], edad=info['edad'], fecha_nacimiento=info['fecha_nacimiento'], descripcion=info['descripcion'],autor=info['autor'],imagen=info['imagen'])
            futbolista.save()
            return redirect('inicio:buscar_futbolista')
            mensaje = f'Se creó el/la futbolista {futbolista.nombre}'
        else:
            return render(request, 'inicio/crear_futbolista.html', {'formulario' : formulario})
    
    formulario = CrearFutbolistaFormulario()
    return render(request, 'inicio/crear_futbolista.html', {'formulario': formulario, 'mensaje': mensaje})

def buscar_futbolista(request):
    
    formulario = BuscarFutbolistaFormulario(request.GET)
    if formulario.is_valid():
        nombre_a_buscar = formulario.cleaned_data['nombre']
        listado_de_futbolistas = Futbolista.objects.filter(nombre__icontains=nombre_a_buscar)
        
    formulario = BuscarFutbolistaFormulario()
    return render(request, 'inicio/futbolistas.html', {'formulario': formulario, 'futbolistas': listado_de_futbolistas})
    

def crear_hockista(request):
    mensaje = ''
    
    if request.method == 'POST':
        formulario = CrearHockistaFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            hockista = Hockista(nombre=info['nombre'], edad=info['edad'], fecha_nacimiento=info['fecha_nacimiento'])
            hockista.save()
            mensaje = f'Se creó el/la hockista {hockista.nombre}'
        else:
            return render(request, 'inicio/crear_hockista.html', {'formulario': formulario})
    
    formulario = CrearHockistaFormulario()
    return render(request, 'inicio/crear_hockista.html', {'formulario': formulario, 'mensaje': mensaje})

def crear_voleibolista(request):
    mensaje = ''
    
    if request.method == 'POST':
        formulario = CrearVoleibolistaFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            voleibolista = Voleibolista(nombre=info['nombre'], edad=info['edad'], fecha_nacimiento=info['fecha_nacimiento'])
            voleibolista.save()
            mensaje = f'Se creó el/la voleibolista {voleibolista.nombre}'
        else:
            return render(request, 'inicio/crear_voleibolista.html', {'formulario': formulario})
    
    formulario = CrearVoleibolistaFormulario()
    return render(request, 'inicio/crear_voleibolista.html', {'formulario': formulario, 'mensaje': mensaje})

class DetalleFutbolista(DetailView):
    model = Futbolista
    template_name = "inicio/detalle_futbolista.html"
...

class ModificarFutbolista(LoginRequiredMixin,UpdateView):
    model = Futbolista
    fields = ['nombre', 'edad', 'fecha_nacimiento', 'descripcion', 'autor', 'imagen']
    template_name = "inicio/modificar_futbolista.html"
    success_url = reverse_lazy('inicio:futbolistas')
...

class EliminarFutbolista(LoginRequiredMixin,DeleteView):
    model = Futbolista
    template_name = "inicio/eliminar_futbolista.html"
    success_url = reverse_lazy('inicio:futbolistas')
...

