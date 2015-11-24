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
	eliminado           = models.BooleanField(default=False)

	def __str__(self):
		return self.nombre

class Empleado(models.Model):
	nombreEmpleado		= models.CharField(max_length=15)
	idRol				= models.ForeignKey('Administrador')
	eliminado           = models.BooleanField(default=False)

	def __str__(self):
	return self.nombreEmpleado	

class Cargo(models.Model):
	idCargo             = models.IntegerField()
	tipo 				= models.CharField(max_length=15)
	salario  		    = models.IntegerField()
	turno               = models.CharField(max_length=15)
	rango        		= models.CharField(max_length=15)
	email    			= models.CharField(max_length=40)
	descuento			= models.IntegerField()
	eliminado           = models.BooleanField(default=False)
	"""docstring for Cargo"""
	def __str__(self):
		return self.idCargo

class Parametro(model.Model):
	atributo        =models.CharField(max_length=50)
    descripcion     =models.CharField(max_length=200)
    estadoParametro =models.CharField(max_length=1)

	def __str__(self):
		return self.atributo

class ValorParametro(model.Model):
	valor                =models.CharField(max_length=30)
    parametro            =models.ForeignKey('Parametro')
    orden                =models.CharField(max_length=3)
    estadoValorParametro =models.CharField(max_length=1)

	def __str__(self):
		return self.valor

class Usuario(models.Model):
	idUsuario			= models.IntegerField()

		

# Create your models here.
