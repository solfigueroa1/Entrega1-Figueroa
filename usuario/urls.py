from django.urls import path
from usuario import views

app_name= 'usuario'

urlpatterns = [
    path('login/',views.login, name='login')
]