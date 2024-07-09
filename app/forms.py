from django import forms
from .models import Producto, Direccion, Categoria, Direccion, Orden, Cliente
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UpdateClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ['nombre','apellidos', 'telefono']

class UpdateOrdenForm(forms.ModelForm):

    class Meta:
        model = Orden
        fields = '__all__'
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
    
    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is not None and precio < 0:
            raise forms.ValidationError("El precio no puede ser negativo.")
        return precio

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock is not None and stock < 0:
            raise forms.ValidationError("El stock no puede ser negativo.")
        return stock

class UpdateProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is not None and precio < 0:
            raise forms.ValidationError("El precio no puede ser negativo.")
        return precio

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock is not None and stock < 0:
            raise forms.ValidationError("El stock no puede ser negativo.")
        return stock

class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = '__all__'




