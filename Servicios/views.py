from django.shortcuts import render
from Servicios.models import Servicio
# Create your views here.


def Servicios(request):
    servicios = Servicio.objects.all()
    return render(request, "Servicios/servicios.html", {'servicios': servicios})
