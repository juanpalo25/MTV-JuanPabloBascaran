from msilib.schema import Class
from django.db import models

class Familia(models.Model):
    nombre = models.CharField(max_length=30)
    anios = models.IntegerField()
    creacion = models.DateField(null =True)
