from django.db import models

# Create your models here.

#Modelo para suscriptor
class Suscriptor(models.Model):
    rut = models.CharField(max_length=10,primary_key=True,verbose_name='Rut')
    nombres = models.CharField(max_length=150,verbose_name='Nombres')
    apellidos = models.CharField(max_length=150,verbose_name='Apellidos')
    telefono = models.CharField(max_length=12,verbose_name='Telefono')
    mail = models.CharField(max_length=30,verbose_name='E-Mail')
    donacion = models.CharField(max_length=10,verbose_name='Monto Donacion')
    
    def __str__(self):
        return self.rut