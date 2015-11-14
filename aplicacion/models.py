from django.db import models
from django.core.validators import MaxLengthValidator
from test.test_imageop import MAX_LEN

class Consumo(models.Model):
	fecha 				= models.DateField()
	hora  				= models.DateField()
	descripcionConsumo  = models.CharField(max_length=15)
	valorConsumo		= models.IntegerField()
	idConsumo			= models.IntegerField()
	idEmpleado			= models.ForeignKey('Administrador')
	"""docstring for Consumo"""
	def __str__(self):
		return self.descripcionConsumo

class Administrador(models.Model):
	nombre				= models.CharField(max_length=15)
	idEmpleado			= models.IntegerField()
	password			= models.CharField(max_length=10)
	idRol				= models.IntegerField()

	def __str__(self):
		return self.nombre

class Empleado(models.Model):
	nombreEmpleado		= models.CharField(max_length=15)
	idRol				= models.ForeignKey('Administrador')

	def __str__(self):
	return self.nombreEmpleado	

class Parametro(model.Model):
	idParametro			=models.IntegerField()

	def __str__(self):
		return self.idParametro

class ValorParametro(model.Model):
	idValor				= models.IntegerField()
	idParametro			= models.ForeignKey('Parametro')
	idUsuario			= models.ForeignKey('Usuario')

	def __str__(self):
		return self.idValor

class Usuario(models.Model):
	idUsuario			= models.IntegerField()

		

# Create your models here.
