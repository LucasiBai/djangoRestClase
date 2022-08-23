from rest_framework import serializers
from main.models import Sucursales, Movimientos, Prestamos


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


class PrestamosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamos
        fields = "__all__"
