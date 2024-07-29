from django.db import models
from django.core.exceptions import ValidationError

# Validación para cantidad
def validar_cantidad(value):
    if value < 0:
        raise ValidationError('La cantidad no puede ser negativa.')

# Validación para precio
def validar_precio(value):
    if value <= 0:
        raise ValidationError('El precio debe ser mayor que cero.')

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(validators=[validar_cantidad])
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[validar_precio])

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField()
    cantidad_ingresada = models.PositiveIntegerField(validators=[validar_cantidad])

    def __str__(self):
        return f"{self.producto.nombre} - {self.cantidad_ingresada}"
