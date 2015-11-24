from django.contrib import admin

from aplicacion.models import *

class EmpleadoAdmin(admin.ModelAdmin):
	list_display=('idRol', 'nombre')

class AdministradorAdmin(admin.ModelAdmin):
	list_display=('id', 'nombre', 'password', 'idRol')

class ConsumoAdmin(admin.ModelAdmin):
	list_display=('fecha', 'hora', 'descripcion', 'valor', 'idConsumo')

class CargoAdmin(admin.ModelAdmin):
	list_display=('tipo', 'salario', 'turno', 'cargo', 'email', 'descuento')


admin.site.register(Consumo, ConsumoAdmin)

admin.site.register(Administrador, AdministradorAdmin)

admin.site.register(Empleado, EmpleadoAdmin)

admin.site.register(Cargo, CargoAdmin)

admin.site.register(Parametro)

admin.site.register(ValorParametro)

admin.site.register(Usuario)
