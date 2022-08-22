# importamos serializador y modelo
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from main.api.serializers import SucursalesSerializer
from main.models import Sucursales


# Create your views here.
class SucursalesLists(APIView):
    def get(self, request):
        sucursales = Sucursales.objects.all()
        serializer = SucursalesSerializer(sucursales, many=True)
        if sucursales:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
