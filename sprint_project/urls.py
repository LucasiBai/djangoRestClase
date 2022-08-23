from django.contrib import admin
from main import views as main_views
from django.conf import settings
from django.urls import path, include

from main.api.api import (
    SucursalesLists,
    MovimientosLists,
    MovimientosDetails,
    PrestamosListCliente,
    PrestamosListSucursal,
    api_root,
)


urlpatterns = [
    # Creamos un patrón url, en la raíz del sitio (cadena vacía) desde el que llamaremos a la vista views.home que tiene el nombre home.
    path("", main_views.home, name="home"),
    path("prestamos/", main_views.prestamos, name="prestamos"),
    path("cuentas/", main_views.cuentas, name="cuentas"),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/registro", main_views.registro, name="registro"),
    path("api/sucursales/", SucursalesLists.as_view(), name="api_sucursales"),
    path(
        "api/movimientos/",
        MovimientosLists.as_view(),
        name="api_movimientos",
    ),
    path("api/movimientos/<int:movimiento_id>/", MovimientosDetails.as_view()),
    path(
        "api/prestamos/<int:cliente_id>/",
        PrestamosListCliente.as_view(),
        name="api_prestamos_list",
    ),
    path(
        "api/prestamos_sucursal/<int:sucursal_id>/",
        PrestamosListSucursal.as_view(),
        name="api_prestamos_sucursal",
    ),
    path("api/", api_root, name="api-root"),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
