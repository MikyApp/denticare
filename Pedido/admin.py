from django.contrib import admin
from .models import Pedido, LineaPedido

# Register your models here.
admin.site.register([Pedido,LineaPedido])
