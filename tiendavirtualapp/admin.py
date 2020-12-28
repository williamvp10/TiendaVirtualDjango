from django.contrib import admin
from tiendavirtualapp.models import Categorias,Productos, Clientes, Inventario, Calificaciones

# Register your models here.
admin.site.register(Categorias)
admin.site.register(Productos)
admin.site.register(Clientes)
admin.site.register(Inventario)
admin.site.register(Calificaciones)
