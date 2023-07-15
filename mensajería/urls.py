from django.urls import path
from mensajería import views

urlpatterns = [
    path('mensajes/',views.mensajes, name='mensajes'),
]
