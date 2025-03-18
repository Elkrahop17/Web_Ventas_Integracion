# Generated by Django 5.0.6 on 2024-06-26 15:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animales', '0009_remove_carrito_producto_gato_alter_carrito_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito',
            name='producto_gatos',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='animales.productogatos'),
        ),
        migrations.AddField(
            model_name='carrito',
            name='producto_perros',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='animales.productoperros'),
        ),
        migrations.AlterField(
            model_name='carrito',
            name='producto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='animales.animalproducto'),
        ),
    ]
