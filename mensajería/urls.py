from django.urls import path
from mensajería import views

app_name = 'mensajería'

urlpatterns = [
    path('mensajes/',views.mensajes, name='mensajes'),
    path('mensajes/enviar',views.crear_mensaje, name='crear_mensaje'), 
     
]
