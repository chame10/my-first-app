from django.contrib import admin
from my_project.Apps.GestionEquipos.models import *

# Register your models here.

admin.site.register(Equipo)
admin.site.register(Entrenador)
admin.site.register(Jugador)
