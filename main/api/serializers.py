from rest_framework import serializers
from main.models import Sucursales, Movimientos


class SucursalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursales
        # indicamos que use todos los campos
        fields = "__all__"


class MovimientosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimientos
        # indicamos que use todos los campos
        fields = "__all__"
        # les decimos cuales son los de solo lectura
