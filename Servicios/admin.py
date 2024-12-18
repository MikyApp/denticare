from django.contrib import admin
from .models import Servicio


# Register your models here.
@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('titulo', 'contenido', 'imagen')
    search_fields = ('nombre',)
    list_per_page = 5 #Paginación