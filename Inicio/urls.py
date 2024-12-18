from django.urls import path
from Inicio import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Inicio, name='inicio'),
    path('infoprod/<int:id>', views.ViewProd, name='infoprod'),

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

