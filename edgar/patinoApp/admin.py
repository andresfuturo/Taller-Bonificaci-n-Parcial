from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Paciente, Cita

admin.site.register(Paciente)
admin.site.register(Cita)
