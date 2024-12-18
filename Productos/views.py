from django.shortcuts import render
from .models import Producto
# Create your views here.

def Productos(request):
    producto = Producto.objects.all()
    if  request.method == 'POST':
        dato = request.POST.get('prod')
        producto = Producto.objects.filter(nombre__icontains = dato)
        return render(request, "Productos/productos.html", {'productos': producto, 'query': dato})
    else:
        return render(request, "Productos/productos.html", {'productos': producto})


def ViewProd(request, id):
    infoprod = Producto.objects.get(id = id)
    nombre = infoprod.nombre
    precio = infoprod.precio
    imagen = infoprod.imagen_producto
    return render (request, 'Productos/infoprod.html', {'infoprod': infoprod, 'nombre':nombre, 'precio':precio, 'imagen': imagen})


