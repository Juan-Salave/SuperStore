from django.contrib import admin
from .models import  Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['marca', 'descripcion', 'precio']

admin.site.register(Producto, ProductoAdmin)
