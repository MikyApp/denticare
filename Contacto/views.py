from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

def Contacto(request):
    asunto = 'Consultas de DentiCare'
    
    if request.method == 'POST':
        # Recopilar datos del formulario
        context = {
            'nombre': request.POST['txtnombre'],
            'apellido': request.POST['txtapellido'],
            'celular': request.POST['txtcelular'],
            'email': request.POST['txteamil'],
            'mensaje': request.POST['txtmensaje']
        }
        
        # Renderizar el template HTML
        html_content = render_to_string('Contacto/email_template.html', context)
        text_content = strip_tags(html_content)  # Versión texto plano del HTML
        
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['mpaucarporras@gmail.com']
        
        # Crear el email con contenido alternativo (HTML y texto plano)
        email = EmailMultiAlternatives(
            subject=asunto,
            body=text_content,
            from_email=email_from,
            to=recipient_list
        )
        
        email.attach_alternative(html_content, "text/html")
        email.send()
        
        return render(request, 'Contacto/gracias.html')
    
    return render(request, "Contacto/contacto.html")