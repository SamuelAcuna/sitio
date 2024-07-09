from django.db import models
from django.contrib.auth.models import User
from .choices import *


class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    eliminado = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
    
    def get_email(self):
        if self.user:
            return self.user.email
        else:
            return self.email




class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.IntegerField()
    stock = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    eliminado = models.BooleanField(default=False)
    
    def get_imagen_url(self):
        if self.imagen and hasattr(self.imagen, 'url'):
            return self.imagen.url
        else:
            # URL de imagen por defecto o placeholder
            return '/media/productos/defecto.png'  # Reemplaza con la URL deseada

    def __str__(self):
        return self.nombre
    def get_precio(self):
        return self.precio

    def __str__(self):
        return self.nombre

class Direccion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='direcciones')
    direccion = models.CharField(max_length=255)
    region = models.CharField(max_length=100, choices=REGIONES_CHILE, default="REGION_BIOBIO")
    ciudad = models.CharField(max_length=100, choices=COMUNAS_POR_REGION)
    codigo_postal = models.CharField(max_length=20)
    tipo = models.CharField(max_length=50)  # 'envio' o 'facturacion'
    eliminado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.direccion}, {self.ciudad}, {self.region}"
    def get_region_display(self):
        return dict(REGIONES_CHILE).get(self.region, self.region)

    def get_ciudad_display(self):
        return dict(COMUNAS_POR_REGION.get(self.region, [])).get(self.ciudad, self.ciudad)

class Orden(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    completada = models.BooleanField(default=False)
    estado = models.CharField(max_length=100, choices=ESTADO_ENVIO,default="EN_PREPARACION", null=True, blank=True)
    direccion_envio = models.ForeignKey(Direccion, on_delete=models.SET_NULL, null=True, blank=True)
    total = models.IntegerField(blank=True, null=True)
    eliminado = models.BooleanField(default=False)
    def get_estado(self):
        return dict(ESTADO_ENVIO).get(self.estado)

    def __str__(self):
        return f"Orden {self.id} - Cliente: {self.cliente}"
    
    def calcular_total(self):
        orden_items = OrdenItem.objects.filter(orden=self)
        total = sum(item.cantidad * item.precio for item in orden_items)
        self.total = total
        self.save()
        return total


class OrdenItem(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField()
    precio = models.IntegerField()

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"

class Pago(models.Model):
    orden = models.OneToOneField(Orden, on_delete=models.CASCADE)
    metodo = models.CharField(max_length=50)
    transaccion_id = models.CharField(max_length=100)
    monto = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pago {self.transaccion_id} - Monto: {self.monto}"


