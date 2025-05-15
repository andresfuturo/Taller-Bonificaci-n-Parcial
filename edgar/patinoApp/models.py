from django.db import models

# Create your models here.

class Paciente(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='citas')
    fecha = models.DateTimeField()
    descripcion = models.TextField()

    def __str__(self):
        return f'Cita de {self.paciente.nombre} el {self.fecha}'
