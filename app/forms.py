from django import forms
from .models import Producto, Direccion, Categoria, Direccion, Orden, Cliente
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Orden  # Ajusta esto con el nombre correcto de tu modelo de Pedido

class UpdateClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ['nombre','apellidos', 'telefono']


class OrdenForm(forms.ModelForm):

    class Meta:
        model = Orden
        fields = '__all__'

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = '__all__'

class CrearUsuario(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']
class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'

class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = '__all__';

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto  # Asegúrate de ajustar esto con tu modelo Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'imagen']  # Campos del modelo que deseas incluir en el formulario

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio < 0:
            raise forms.ValidationError("El precio no puede ser negativo.")
        return precio

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock < 0:
            raise forms.ValidationError("El stock no puede ser negativo.")
        return stock;

class ModificarPedidoForm(forms.ModelForm):
    class Meta:
        model = Orden  # Ajusta con el modelo de tu Pedido
        fields = ['cliente', 'total', 'completada']  # Campos que se pueden modificar
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['cliente'].widget.attrs['readonly'] = True  # Cliente no editable desde el formulario
            self.fields['total'].widget.attrs['readonly'] = True    # Total no editable desde el formulario




