from django.shortcuts import redirect
from .carro import Carro
from Productos.models import Producto
from django.http import HttpResponse
# Create your views here.

#Agregar un producto
def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect('productos')


#Eliminar un producto
def eliminar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect('productos')

#Restar un producto
def restar_producto (request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect('productos')

#Limpiar carrito
def limpiar_carro(request,):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect('productos')