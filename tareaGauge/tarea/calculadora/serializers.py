from rest_framework import serializers
from . models import Reto, Jugadores, Usuario, partidas, Gauge

###############################################
############  TAREA 3.3  ######################
###############################################

class GaugeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gauge
        fields = ('id', 'user_name', 'puntaje')

###############################################
############  TAREA 1.4 REST ##################
###############################################

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'password')

class PartidasSerializer(serializers.ModelSerializer):
    class Meta:
        model = partidas
        fields = ('id', 'fecha', 'usuario', 'minutos_jugados', 'puntaje')

###############################################


class RetoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reto
        fields = ('id','nombre','minutos_jugados')

class JugadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Jugadores
        fields = ('id','grupo','num_lista')