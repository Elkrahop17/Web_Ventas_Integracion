from django.contrib import admin
from .models import AnimalProducto, ProductoPerros, ProductoGatos, Carrito
# Register your models here.
admin.site.register(AnimalProducto)
admin.site.register(ProductoPerros)
admin.site.register(ProductoGatos)
admin.site.register(Carrito)