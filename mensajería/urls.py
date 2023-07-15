from django.urls import path
from mensajería import views

app_name = 'mensajería'

urlpatterns = [
    path('mensajes/', views.mensaje, name = 'mensajes'),
    path('mensajes/<int:pk>',views.Mensajes.as_view(), name='listado_mensajes'),
    path('mensajes/enviar',views.crear_mensaje, name='crear_mensaje'),
    
]
