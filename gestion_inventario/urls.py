from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, ProductoViewSet, ProveedorViewSet, InventarioViewSet, custom_api

# Crea un router para manejar las rutas automáticamente
router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'proveedores', ProveedorViewSet)
router.register(r'inventarios', InventarioViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Incluye las rutas del router
    path('custom-api/', custom_api, name='custom_api'),  # Ruta para la API personalizada
]
