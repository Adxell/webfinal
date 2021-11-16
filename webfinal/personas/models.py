from django.db import models
from django.db.models.base import Model

# Create your models here.


class Personas(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    correo=models.EmailField(max_length=50, unique=True)
    fecha_nacimiento=models.DateField(max_length=50)
    def __str__(self):
        return self.nombre+"-"+self.nombre

class Reporte(models.Model):
    fecha =models.DateField(max_length=60)
    persona=models.ForeignKey(Personas, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.fecha



