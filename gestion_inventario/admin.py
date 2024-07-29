from django.contrib import admin
from .models import Categoria, Producto, Proveedor, Inventario

# Registra cada modelo para que aparezca en el panel de administración de Django
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(Inventario)
