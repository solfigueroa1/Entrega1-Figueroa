from django.urls import path
from inicio import views


app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('futbolistas/',views.buscar_futbolista, name='futbolistas'),
    path('futbolistas/crear/', views.crear_futbolista, name='crear_futbolista'),
    path('hockistas/crear/', views.crear_hockista, name='crear_hockista'),
    path('voleibolistas/crear/', views.crear_voleibolista, name='crear_voleibolista'),
]
