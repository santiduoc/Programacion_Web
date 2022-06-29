from rest_framework import serializers
from core.models import Suscriptor
class SuscriptorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suscriptor
        fields = ['rut', 'nombres', 'apellidos', 'telefono' , 'mail', 'donacion']