from rest_framework import permissions
from .models import ids


class esEmpleado(permissions.BasePermission):
    def has_permission(self, request, view):
        username = request.user
        return ids.objects.filter(username=username).first().tipo == "empleado"
