from django.urls import path
from . import views


urlpatterns = [
    path('', views.Contacto, name='contacto'),
]


