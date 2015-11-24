from django import forms
from django.forms import ModelForm
from aplicacion.models import *

class ParametroForm(forms.Form):
    pass

class EmpleadoForm(ModelForm): 
   class Meta:
        model=Empleado
        exclude=["eliminado"]

class CargoForm(ModelForm): 
   class Meta:
        model=Cargo
        exclude=["eliminado"]


class ConsumoForm(ModelForm):
   class Meta:
   	    model=Consumo
   	    exclude=["eliminado"]