from datetime import date

# importamos serializador y modelo
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from main.api.serializers import (
    SucursalesSerializer,
    MovimientosSerializer,
    PrestamosSerializer,
)
from main.models import Sucursales, Movimientos, Prestamos, ids
from main.permissions import esEmpleado


# Create your views here.
class SucursalesLists(APIView):
    def get(self, request):
        sucursales = Sucursales.objects.all()
        serializer = SucursalesSerializer(sucursales, many=True)
        if sucursales:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class MovimientosLists(APIView):
    permission_classes = [permissions.IsAuthenticated, esEmpleado]

    def get(self, request):
        movimientos = Movimientos.objects.all()
        serializer = MovimientosSerializer(movimientos, many=True)
        if movimientos:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        data = request.data
        data["fecha"] = date.today().strftime("%Y-%m-%d")
        serializer = MovimientosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovimientosDetails(APIView):
    permission_classes = [permissions.IsAuthenticated, esEmpleado]

    def delete(self, request, movimiento_id):
        movimiento = Movimientos.objects.filter(pk=movimiento_id).first()
        if movimiento:
            serializer = MovimientosSerializer(movimiento)
            movimiento.delete()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, movimiento_id):
        movimiento = Movimientos.objects.filter(pk=movimiento_id).first()
        serializer = MovimientosSerializer(movimiento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PrestamosListCliente(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, cliente_id):
        # podemos chequear que un cliente solo haga GET para sus propios prestamos
        username = request.user
        owner = cliente_id
        try:
            user = ids.objects.filter(username=username).first()
            dni = user.cliente_id
        except:
            dni = -1
        if dni == owner or user.tipo == "empleado":

            prestamos = Prestamos.objects.filter(cliente_id=cliente_id)
            serializer = PrestamosSerializer(prestamos, many=True)
            if prestamos:
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(
                    "no hay prestamos asociados a este cliente",
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            return Response(
                "no coincide el dni ni es empleado", status=status.HTTP_404_NOT_FOUND
            )
