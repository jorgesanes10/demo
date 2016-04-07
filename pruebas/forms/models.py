from django.db import models

class Empleado(models.Model):
	cedula = models.CharField(max_length=20)
	nombre = models.CharField(max_length=50)
	sueldo = models.FloatField()
	fecha_ing = models.DateField()