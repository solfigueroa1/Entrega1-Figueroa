from django.contrib import admin
from inicio.models import Futbolista, Hockista, Voleibolista

# Register your models here.

admin.site.register([Futbolista, Hockista, Voleibolista])
