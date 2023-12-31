from django.urls import path
from inicio import views


app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('about/', views.about, name='about'),
    path('futbolistas/',views.buscar_futbolista, name='futbolistas'),
    path('futbolistas/crear/', views.crear_futbolista, name='crear_futbolista'),
    path('hockistas/crear/', views.crear_hockista, name='crear_hockista'),
    path('voleibolistas/crear/', views.crear_voleibolista, name='crear_voleibolista'),
    path('futbolistas/<int:pk>/',views.DetalleFutbolista.as_view(), name='detalle_futbolista'),
    path('futbolistas/<int:pk>/modificar/',views.ModificarFutbolista.as_view(), name='modificar_futbolista'),
    path('futbolistas/<int:pk>/eliminar/',views.EliminarFutbolista.as_view(), name='eliminar_futbolista'),

]

