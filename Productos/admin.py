from django.contrib import admin
from .models import Categoria, Producto

# Register your models here.
admin.site.site_header = 'DENTICARE'
admin.site.site_title = 'DENTICARE'
admin.site.index_title = 'Gestion de productos - DentiCare'

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('nombre', 'imagen', 'created', 'updated')
    search_fields = ('nombre',)
    list_per_page = 5 #Paginación

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('nombre', 'categorias', 'sku', 'precio', 'marca', 'codigo_interno', 'presentacion','descripcion', 'imagen_producto', 'stock', 'disponibilidad', 'created', 'updated')
    search_fields = ('nombre',)
    list_per_page = 5 #Paginación
#alt+z
