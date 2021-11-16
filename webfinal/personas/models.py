from django.db import models
from django.db.models.base import Model

# Create your models here.


class Personas(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=50, unique=True)
    age=models.DateField(max_length=50)
    