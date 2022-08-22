from rest_framework import serializers
from main.models import Sucursales


class SucursalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursales
        # indicamos que use todos los campos
        fields = "__all__"
