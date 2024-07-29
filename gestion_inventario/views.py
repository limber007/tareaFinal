from rest_framework import viewsets
from .models import Categoria, Producto, Proveedor, Inventario
from .serializers import CategoriaSerializer, ProductoSerializer, ProveedorSerializer, InventarioSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


# ViewSet para manejar las operaciones CRUD de Categoria
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()  # Obtiene todos los objetos de Categoria
    serializer_class = CategoriaSerializer  # Usa el serializer correspondiente

# ViewSet para manejar las operaciones CRUD de Producto
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

# ViewSet para manejar las operaciones CRUD de Proveedor
class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

# ViewSet para manejar las operaciones CRUD de Inventario
class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer


# API personalizada que devuelve el total de productos
@api_view(['GET'])
def custom_api(request):
    total_productos = Producto.objects.count()  # Cuenta el número total de productos
    return Response({"total_productos": total_productos})  # Devuelve el total en formato JSON