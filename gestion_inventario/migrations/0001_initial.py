# Generated by Django 5.0.7 on 2024-07-29 00:17

import django.db.models.deletion
import gestion_inventario.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('cantidad', models.PositiveIntegerField(validators=[gestion_inventario.models.validar_cantidad])),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, validators=[gestion_inventario.models.validar_precio])),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_inventario.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_ingreso', models.DateField()),
                ('cantidad_ingresada', models.PositiveIntegerField(validators=[gestion_inventario.models.validar_cantidad])),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_inventario.producto')),
            ],
        ),
    ]
