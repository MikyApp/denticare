from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Carrito.carro import Carro
from Pedido.models import LineaPedido, Pedido
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

# Agrega esta función antes de procesar_pedido
def formatear_lineas_pedido(lineas_pedido):
    return ", ".join([f"{linea.cantidad} unidades de {linea.producto.nombre}" for linea in lineas_pedido])

@login_required(login_url="autenticacion/logear")
def procesar_pedido(request):
    pedido = Pedido.objects.create(user=request.user)
    carro = Carro(request)
    lineas_pedido = list()
    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(
            producto_id=key,
            cantidad = value['cantidad'],
            user=request.user,
            pedido = pedido
        ))

    LineaPedido.objects.bulk_create(lineas_pedido)

    # Usa la nueva función aquí
    lineas_texto = formatear_lineas_pedido(lineas_pedido)

    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        lineas_texto=lineas_texto,  # Agrega esto
        nombreusuario=request.user.username,
        emailusuario=request.user.email
    )

    messages.success(request, 'El pedido se ha creado correctamente')

    return redirect("../productos")

def enviar_mail(**kwargs):
    asunto = "Nuevo pedido DentiCare - Gracias"
    mensaje= render_to_string("emails/pedido.html", {
        "pedido": kwargs.get("pedido"),
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "lineas_texto": kwargs.get("lineas_texto"),  # Y aquí también
        "nombreusuario":kwargs.get("nombreusuario"),
    })

    mensaje_texto = strip_tags(mensaje)
    from_email="miguelpaucar987@gmail.ccom"
    to='mpaucarporras@gmail.com'

    send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)