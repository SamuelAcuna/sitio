from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Orden, Cliente, OrdenItem, Direccion
from .forms import *
from .choices import REGIONES_CHILE, COMUNAS_POR_REGION
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .services import OrderService
from django.http import Http404
import requests
from django.http import JsonResponse


def modificarcliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)  # Cambia cliente a Cliente
    form = UpdateClienteForm(instance=cliente)  # Pasar la instancia del cliente al formulario

    if request.method == "POST":
        form = UpdateClienteForm(data=request.POST, files=request.FILES, instance=cliente)  # Usar la instancia del cliente
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente Modificado')
            return redirect('tabla_clientes') 

    datos = {
        "cliente": cliente,
        "form": form,  
    }
    return render(request, 'dash/modificarcliente.html', datos)

def modificarorden(request,id):
    orden=get_object_or_404(Orden, id=id)
    form = UpdateOrdenForm(instance=orden)  # Pasar la instancia del producto al formulario

    if request.method == "POST":
        form = UpdateOrdenForm(data=request.POST, files=request.FILES, instance=orden)  # Usar la instancia del producto
        if form.is_valid():
            form.save()
            messages.success(request, 'Orden Modificada')
            return redirect('tabla_ordenes')  

   
    
    items = OrdenItem.objects.filter(orden=orden)
    datos={
         "orden":orden,
         'items':items,
         "forms": form,
     }
    return render(request, 'dash/modificarorden.html',datos)
    
def detalleorden(request,id):
    orden=get_object_or_404(Orden, id=id)
    items = OrdenItem.objects.filter(orden=orden)
    datos={
         "orden":orden,
         'items':items
     }
    return render(request, 'app/detalleorden.html',datos)

def misordenes(request):
    cliente = Cliente.objects.get(user=request.user)
    ordenes = Orden.objects.filter(cliente=cliente)
    datos={
        'cliente':cliente,
        'ordenes':ordenes
    }
    
    return render(request, 'app/misordenes.html',datos)

def misdirecciones(request):
    cliente = Cliente.objects.get(user=request.user)
    direcciones = Direccion.objects.filter(cliente=cliente, eliminado=False)
    
    if request.method == "POST":
        accion = request.POST.get("accion")
        direccion_id = request.POST.get("direccionid")
        nueva_direccion = request.POST.get("nueva_direccion")
        nueva_region = request.POST.get("nueva_region")
        nueva_ciudad = request.POST.get("nueva_ciudad")
        nuevo_codigo_postal = request.POST.get("nuevo_codigo_postal")

        if accion == 'eliminar':
            try:
                direccion = get_object_or_404(Direccion, id=direccion_id)
                direccion.eliminado = True
                direccion.save()
                messages.success(request, 'La dirección ha sido eliminada correctamente.')
            except (KeyError, Direccion.DoesNotExist):
                messages.error(request, 'Error al eliminar la dirección.')
            return redirect("misdirecciones")
        
        elif accion == 'agregar':
            if nueva_direccion and nueva_region and nueva_ciudad and nuevo_codigo_postal:
                Direccion.objects.create(
                    cliente=cliente,
                    direccion=nueva_direccion,
                    region=nueva_region,
                    ciudad=nueva_ciudad,
                    codigo_postal=nuevo_codigo_postal,
                    tipo='envio'
                )
                messages.success(request, 'La nueva dirección ha sido agregada correctamente.')
            else:
                messages.error(request, 'Por favor, complete todos los campos para agregar una nueva dirección.')
            return redirect('misdirecciones')
    
    datos = {
        'cliente': cliente,
        'direcciones': direcciones,
        'REGIONES_CHILE': REGIONES_CHILE,
        'COMUNAS_POR_REGION': COMUNAS_POR_REGION,
    }
    return render(request, 'app/misdirecciones.html', datos)

def perfil(request):
    cliente = Cliente.objects.get(user=request.user)

    form=UpdateClienteForm(instance=cliente)
    datos={
        "form":form,
        "cliente":cliente
    }

    if request.method=="POST":
        form=UpdateClienteForm(data=request.POST, files=request.FILES, instance=cliente)
        if form.is_valid():
            form.save()
            messages.warning(request,'Datos Modificados')
            return redirect(to='perfil')
    
    return render(request, 'app/perfil.html',datos)

def about(request):
    return render(request, 'app/about.html')


def base(request):
    return render(request, 'app/base.html')


@login_required
def cart(request):
    if request.method == 'POST':
        accion = request.POST.get('accion')
        
        if accion == 'actualizar':
            try:
                ordenitem_id = request.POST.get('ordenitemid')
                product_id = request.POST.get('productoid')
                cantidad = int(request.POST.get('cantidad'))
                
                
                # Obtener el producto y verificar el stock
                producto = Producto.objects.get(id=product_id)
                if cantidad > producto.stock:
                    cantidad = producto.stock  # Asignar la cantidad máxima de stock disponible
                    messages.warning(request, f'La cantidad solicitada excede el stock disponible. Se ha ajustado a {producto.stock}.')
                    producto = Producto.objects.get(id=product_id)
                    precio_item = producto.precio * cantidad
                    
                    # Obtener o crear el OrdenItem y actualizarlo
                    ordenitem = OrdenItem.objects.get(id=ordenitem_id)
                    ordenitem.cantidad = cantidad
                    ordenitem.precio = precio_item
                    ordenitem.save()
                    
                    
                    return redirect("cart")
                    
                
                
                # Obtener el producto y calcular el precio del item
                producto = Producto.objects.get(id=product_id)
                precio_item = producto.precio * cantidad
                
                # Obtener o crear el OrdenItem y actualizarlo
                ordenitem = OrdenItem.objects.get(id=ordenitem_id)
                ordenitem.cantidad = cantidad
                ordenitem.precio = precio_item
                ordenitem.save()
                
                messages.success(request, 'El item ha sido actualizado correctamente.')
                return redirect("cart")
            except (KeyError, Producto.DoesNotExist, OrdenItem.DoesNotExist):
                messages.error(request, 'Error al actualizar el item.')
                return redirect("cart")
            
        elif accion == 'eliminar':
            try:
                ordenitem_id = request.POST.get('ordenitemid')
                ordenitem = get_object_or_404(OrdenItem, id=ordenitem_id)
                ordenitem.delete()
                
                messages.success(request, 'El item ha sido eliminado correctamente.')
                return redirect("cart")
            except (KeyError, OrdenItem.DoesNotExist):
                messages.error(request, 'Error al eliminar el item.')
                return redirect("cart")
                
        else:  # Añadir nuevo item al carrito
            try:
                cliente = Cliente.objects.get(user=request.user)
                product_id = request.POST.get('productoid')
                cantidad = int(request.POST.get('cantidad'))
                producto = Producto.objects.get(id=product_id)
                
                # Verificar el stock
                if cantidad > producto.stock:
                    cantidad = producto.stock  # Asignar la cantidad máxima de stock disponible
                    messages.warning(request, f'La cantidad solicitada excede el stock disponible. Se ha ajustado a {producto.stock}.')
                # Calcular el precio del item
                precio_item = producto.precio * cantidad
                
                orden_incompleta = Orden.objects.filter(cliente=cliente, completada=False).first()
                
                if orden_incompleta:
                    item_existente = OrdenItem.objects.filter(orden=orden_incompleta, producto=producto).first()
                    if item_existente:
                        nueva_cantidad = item_existente.cantidad + cantidad
                        if nueva_cantidad > producto.stock:
                            nueva_cantidad = producto.stock  # Asignar la cantidad máxima de stock disponible
                            messages.warning(request, f'La cantidad solicitada excede el stock disponible. Se ha ajustado a {producto.stock}.')
                        item_existente.cantidad = nueva_cantidad
                        item_existente.precio = producto.precio * nueva_cantidad
                        item_existente.save()
                    else:
                        OrdenItem.objects.create(orden=orden_incompleta, producto=producto, cantidad=cantidad, precio=precio_item)
                
                else:
                    nueva_orden = Orden.objects.create(cliente=cliente)
                    item = OrdenItem.objects.create(orden=nueva_orden, producto=producto, cantidad=cantidad, precio=precio_item)
                
                messages.success(request, 'El item ha sido añadido al carrito.')
                return redirect("cart")
            except KeyError:
                messages.error(request, 'Falta información en el formulario.')
                return redirect("cart")
            except Cliente.DoesNotExist:
                messages.error(request, 'Debe iniciar sesión como cliente.')
                return redirect("cart")
            except Producto.DoesNotExist:
                messages.error(request, 'El producto seleccionado no existe.')
                return redirect("cart")
    
    cliente = Cliente.objects.get(user=request.user)
    ordenitems = OrdenItem.objects.filter(orden__cliente=cliente, orden__completada=False)
    datos = {'ordenitems': ordenitems}
    return render(request, 'app/cart.html', datos)

def checkout(request):
    cliente = Cliente.objects.get(user=request.user)
    orden_incompleta = Orden.objects.filter(cliente=cliente, completada=False).first()
    direcciones = Direccion.objects.filter(cliente=cliente)
    
    if not orden_incompleta:
        messages.error(request, "No hay una orden incompleta.")
        return redirect('shop')
    
    orden_incompleta.calcular_total()
    orden_incompleta.save()
    ordenes = OrdenItem.objects.filter(orden=orden_incompleta)
    
    if request.method == "POST":
        direccion_id = request.POST.get("direccion")
        nueva_direccion = request.POST.get("nueva_direccion")
        nueva_region = request.POST.get("nueva_region")
        nueva_ciudad = request.POST.get("nueva_ciudad")
        nuevo_codigo_postal = request.POST.get("nuevo_codigo_postal")
        
        if direccion_id:
            direccion = Direccion.objects.get(id=direccion_id)
            orden_incompleta.direccion_envio = direccion  # Asigna la dirección seleccionada a la orden incompleta
            orden_incompleta.save()
            return redirect('checkout')
        
        if nueva_direccion and nueva_region and nueva_ciudad and nuevo_codigo_postal:
            # Guarda la nueva dirección en la base de datos
            direccion = Direccion.objects.create(
                cliente=cliente,
                direccion=nueva_direccion,
                region=nueva_region,
                ciudad=nueva_ciudad,
                codigo_postal=nuevo_codigo_postal,
                tipo='envio'
            )
            orden_incompleta.direccion_envio = direccion  # Asigna la nueva dirección a la orden incompleta
            orden_incompleta.save()
            return redirect('checkout')
        else:
            messages.error(request, "Por favor completa todos los campos para la nueva dirección.")
    
    datos = {
        'cliente': cliente,
        'orden': orden_incompleta,
        'ordenes': ordenes,
        'direcciones': direcciones,
        'REGIONES_CHILE': REGIONES_CHILE,
        'COMUNAS_POR_REGION': COMUNAS_POR_REGION,
    }
    
    return render(request, 'app/checkout.html', datos)
def cliente(request):
    return render(request, 'app/cliente.html')

def contact(request):
    return render(request, 'app/contact.html')

def index(request):
    return render(request, 'app/index.html')

def producto(request,id):
    producto = get_object_or_404(Producto, id=id)
    datos={
        'p':producto
    }
    return render(request, 'app/producto.html', datos)

def shop(request):
    productos=Producto.objects.filter(eliminado = False)
    
    datos={
        
        "productos":productos
    }
    return render(request, 'app/shop.html', datos)

def thankyou(request):
    if request.method == 'POST':
        orden_id = request.POST.get('orden')
        direccion_id = request.POST.get('direccion_seleccionada')  # Asegúrate de que el nombre coincida con el campo del formulario
        
        try:
            orden = Orden.objects.get(id=orden_id)
            
            # Si se proporcionó una dirección ID, asigna la dirección a la orden
            if not direccion_id:
                messages.error(request, "Debe seleccionar una dirección de envío.")
                return redirect('checkout')
            if direccion_id:
                direccion = Direccion.objects.get(id=direccion_id)
                orden.direccion_envio = direccion
                orden.save()
            
            # Completa la orden utilizando tu servicio
            order_service = OrderService(orden_id)
            order_service.complete_order()
            
            datos = {'orden': orden}
            
            # Renderiza la página de agradecimiento con los datos de la orden
            return render(request, 'app/thankyou.html', datos)
        
        except Orden.DoesNotExist:
            raise Http404("La orden o la dirección no existe.")
        except Direccion.DoesNotExist:
            raise Http404("La dirección seleccionada no existe.")
        except Exception as e:
            # Maneja otros posibles errores aquí
            messages.error(request, f"Error al procesar la orden: {str(e)}")
            return redirect('shop') 


def get_local_time_view(request):
    local_time = get_local_time()  # Obtener la hora local
    data = {'local_time': local_time}
    return JsonResponse(data)

def get_local_time():
    url = 'http://worldtimeapi.org/api/ip/'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción para errores HTTP
        
        data = response.json()
        return data['datetime']  # Devuelve la hora local en formato ISO8601
    except requests.exceptions.RequestException as e:
        print(f'Error al obtener la hora local: {e}')
        return None

API_KEY = 'edfdc909456a8af1bb840533'

def get_exchange_rate(base_currency, target_currency):
    url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base_currency}'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción para errores HTTP
        data = response.json()
        if 'conversion_rates' in data and target_currency in data['conversion_rates']:
            return data['conversion_rates'][target_currency]
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f'Error en la solicitud a la API de tipo de cambio: {e}')
        return None
def get_random_joke():
    url = 'https://official-joke-api.appspot.com/random_joke'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    return None
def dash(request):
    clp_to_usd_rate = get_exchange_rate('USD', 'CLP')
    clp_to_eur_rate = get_exchange_rate('EUR', 'CLP')
    random_joke = get_random_joke()
    ordenes=Orden.objects.filter(eliminado = False)
    context = {
        'clp_to_usd_rate': clp_to_usd_rate,
        'clp_to_eur_rate':clp_to_eur_rate,
        'random_joke': random_joke,
        'local_time': get_local_time(),
        "ordenes":ordenes
    }
    return render(request, 'dash/index.html', context)

def register(request):
    if request.method == 'POST':
        form = CrearUsuario(request.POST)
        if form.is_valid():
            user = form.save()
            Cliente.objects.create(
                user=user,
                nombre=user.first_name,
                apellidos=user.last_name,
                email=user.email
            )
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')  # Redirige a la página principal u otra página
    else:
        form = CrearUsuario()
    return render(request, 'dash/register.html', {'form': form})

def password(request):
    return render(request, 'dash/password.html')

def tabla_clientes(request):
    clientes = Cliente.objects.filter(eliminado=False)
    
    if request.method == "POST":
        cliente_id = request.POST.get("clienteid")
        try:
            cliente = get_object_or_404(Cliente, id=cliente_id)
            cliente.eliminado = True
            cliente.save()
            messages.success(request, 'El cliente ha sido eliminado correctamente.')
        except Exception as e:
            messages.error(request, f'Error al eliminar cliente: {str(e)}')

    datos = {
        "clientes": clientes
    }

    return render(request, 'dash/tabla_clientes.html', datos)

def tabla_ordenes(request):
    ordenes=Orden.objects.filter(eliminado = False)
    if request.method == "POST":
        orden = request.POST.get("ordenid")
        try:
            orden = get_object_or_404(Orden, id=orden)
            orden.eliminado = True
            orden.save()
            messages.success(request, 'La orden ha sido eliminado correctamente.')
        except:
            messages.error(request, 'Error al eliminar la orden.')
    datos={
        "ordenes":ordenes
    }
    return render(request, 'dash/tabla_ordenes.html',datos)


def tabla_producto(request):
    if request.method == "POST":
        accion = request.POST.get("accion")
        producto_id = request.POST.get("producto_id")

        if accion == "eliminar":
            try:
                producto = get_object_or_404(Producto, id=producto_id)
                producto.eliminado = True
                producto.save()
                messages.success(request, 'El producto ha sido eliminado correctamente.')
            except Producto.DoesNotExist:
                messages.error(request, 'El producto no existe o ya ha sido eliminado.')
            except Exception as e:
                messages.error(request, f'Error al eliminar el producto: {str(e)}')

        elif accion == "agregar_stock":
            cantidad = int(request.POST.get("cantidad", 0))
            if cantidad <= 0:
                messages.error(request, 'La cantidad debe ser mayor que cero para agregar stock.')
            else:
                producto = get_object_or_404(Producto, id=producto_id)
                producto.stock += cantidad
                producto.save()
                messages.success(request, f'Se agregaron {cantidad} unidades al stock correctamente.')

    productos = Producto.objects.filter(eliminado=False)
    datos = {
        "productos": productos
    }

    return render(request, 'dash/tabla_producto.html', datos)

def agregar_producto(request):
    form=ProductoForm()

    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto agregado correctamente.')
            return redirect('tabla_producto')  
    else:
        form = ProductoForm()

   
    datos={
        "form":form
    }
    return render(request, 'dash/agregar_producto.html',datos)

def agregar_categoria(request):
    form=CategoriaForm()

    if request.method=="POST":
        form=CategoriaForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to="tabla_producto")

    datos={
        "form":form
    }
    return render(request, 'dash/agregar_producto.html',datos)
def agregar_orden(request):
    form=OrdenForm()

    if request.method=="POST":
        form=OrdenForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to="tabla_producto")

    datos={
        "form":form
    }
    return render(request, 'dash/agregar_producto.html',datos)
def modificar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    form = UpdateProductoForm(instance=producto)  # Pasar la instancia del producto al formulario

    if request.method == "POST":
        form = UpdateProductoForm(data=request.POST, files=request.FILES, instance=producto)  # Usar la instancia del producto
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto Modificado')
            return redirect('tabla_producto')  # Nombre de la URL a la que quieres redirigir después de guardar

    datos = {
        "producto": producto,
        "forms": form,  # Corregir el nombre de la variable
    }
    return render(request, 'dash/modificar_producto.html', datos)

def formulario_cliente(request):
    return render(request, 'dash/formulario_cliente.html')

def modificar_cliente(request):
    return render(request, 'dash/modificar_cliente.html')



