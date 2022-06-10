from django import forms
from django.forms import ModelForm
from .models import Vehiculo

#creamos nuestra clase para el formulario desde la base de datos
class VehiculoForm(ModelForm):
    class Meta:
        model= Vehiculo
        fields = ['patente','marca','modelo','categoria']