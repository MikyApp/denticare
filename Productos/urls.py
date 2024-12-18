from django.urls import path
from Productos import views


urlpatterns = [
    path('', views.Productos, name='productos'),
    path('infoprod/<int:id>', views.ViewProd, name='infoprod'),

]



