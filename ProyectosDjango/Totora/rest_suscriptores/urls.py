from django.urls import path
from rest_suscriptores.views import lista_suscriptores,detalle_suscriptor


urlpatterns = [
    path('lista_suscriptores',lista_suscriptores,name="lista_suscriptores"),
    path('detalle_suscriptor/<id>',detalle_suscriptor,name="detalle_suscriptor"),

]