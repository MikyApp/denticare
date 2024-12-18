from django.shortcuts import render, HttpResponse
from Carrito.carro import Carro
from Servicios.models import Servicio
from Productos.models import Producto

# Create your views here.


def Inicio(request):
    carro = Carro(request)
    servicios = Servicio.objects.all()
    productos = Producto.objects.all()

    return render(request, "Inicio/inicio.html",{'servicios':servicios, 'products':productos})

def ViewProd(request, id):
    infoprod = Producto.objects.get(id = id)
    nombre = infoprod.nombre
    precio = infoprod.precio
    imagen = infoprod.imagen_producto
    return render (request, 'Productos/infoprod.html', {'infoprod': infoprod, 'nombre':nombre, 'precio':precio, 'imagen': imagen})






