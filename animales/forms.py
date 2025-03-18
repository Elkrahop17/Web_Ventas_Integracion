from django import forms
from .models import AnimalProducto, ProductoPerros, ProductoGatos


class ProductoForm(forms.ModelForm):
    class Meta:
        model = AnimalProducto
        fields = ['nombre', 'precio', 'stock', 'imagen', 'minutos']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'minutos': forms.NumberInput(attrs={'class': 'form-control'}),
        }



# Formulario para ProductoPerros
class ProductoPerrosForm(forms.ModelForm):
    class Meta:
        model = ProductoPerros
        fields = ['nombre', 'precio', 'stock', 'imagen', 'minutos']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'minutos': forms.NumberInput(attrs={'class': 'form-control'}),
        }


# Formulario para ProductoGatos
class ProductoGatosForm(forms.ModelForm):
    class Meta:
        model = ProductoGatos
        fields = ['nombre', 'precio', 'stock', 'imagen', 'minutos']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'minutos': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        
        