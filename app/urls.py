
from django.urls import path, include
from .views import *

#PARA TRABAJAR CON IMAGENES
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('detalleorden/<id>', detalleorden, name='detalleorden'),
    path('misordenes/', misordenes, name='misordenes'),
    path('misdirecciones/', misdirecciones, name='misdirecciones'),
    path('perfil/', perfil, name='perfil'),
    path('about/', about, name='about'),
    path('base/', base, name='base'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('cliente/', cliente, name='cliente'),
    path('contact/', contact, name='contact'),
    path('', index, name='index'),
    path('producto/<id>/', producto, name='producto'),
    path('shop/', shop, name='shop'),
    path('thankyou/', thankyou, name='thankyou'),
    path('dash/', dash, name='dash'),
    path('dash/register/', register, name='register'),
    path('dash/password/', password, name='password'),
    path('dash/tabla_clientes/', tabla_clientes, name='tabla_clientes'),
    path('dash/tabla_ordenes/', tabla_ordenes, name='tabla_ordenes'),
    path('dash/tabla_producto/', tabla_producto, name='tabla_producto'),
    path('dash/agregar_producto/', agregar_producto, name='agregar_producto'),
    path('dash/agregar_categoria/', agregar_categoria, name='agregar_categoria'),
    path('dash/agregar_orden/', agregar_orden, name='agregar_orden'),
    path('dash/modificar_producto/<id>', modificar_producto, name='modificar_producto'),
    path('dash/formulario_cliente/', formulario_cliente, name='formulario_cliente'),
    path('dash/modificar_cliente/', modificar_cliente, name='modificar_cliente'),
    path('dash/agrega/', agrega, name='agrega'),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)