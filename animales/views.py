from django.shortcuts import render, get_object_or_404, redirect
from .models import AnimalProducto, ProductoPerros, ProductoGatos, Carrito, Pedido, PedidoItem
from .forms import ProductoForm, ProductoPerrosForm, ProductoGatosForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User 
from django.http import HttpResponse

# Create your views here.

#vista del index
def index(request):
    productos = AnimalProducto.objects.all()
    return render(request, 'animales/index.html', {'productos': productos})

#vista de la pag favoritos
def favoritos(request):
    context= {}
    return render(request, 'animales/favoritos.html', context)

#vista de la pag carrito

def ver_carrito(request):
    carrito_items = Carrito.objects.all()
    
    def clean_price(price_str):
        # Elimina el signo de dólar y el separador de miles.
        price_str = price_str.replace('$', '').replace('.', '').replace(',', '.')
        return int(price_str)

    total = 0
    for item in carrito_items:
        if item.producto and item.producto.precio:
            total += clean_price(item.producto.precio) * item.cantidad
        elif item.producto_perros and item.producto_perros.precio:
            total += clean_price(item.producto_perros.precio) * item.cantidad
        elif item.producto_gatos and item.producto_gatos.precio:
            total += clean_price(item.producto_gatos.precio) * item.cantidad

    return render(request, 'animales/carrito.html', {'carrito_items': carrito_items, 'total': total})




# vista agregar productos al carro

def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(AnimalProducto, id=producto_id)
    item, created = Carrito.objects.get_or_create(producto=producto)
    if not created:
        item.cantidad += 1
        item.save()
    return redirect('ver_carrito')

# vista agregar productos al carro perros
def agregar_al_carrito_perro(request, producto_id):
    producto = get_object_or_404(ProductoPerros, id=producto_id)
    item, created = Carrito.objects.get_or_create(producto_perros=producto)
    if not created:
        item.cantidad += 1
        item.save()
    return redirect('ver_carrito')

# vista agregar productos al carro gatos
def agregar_al_carrito_gato(request, producto_id):
    producto = get_object_or_404(ProductoGatos, id=producto_id)
    item, created = Carrito.objects.get_or_create(producto_gatos=producto)
    if not created:
        item.cantidad += 1
        item.save()
    return redirect('ver_carrito')


# vista eliminar productos
def eliminar_del_carrito(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(Carrito, id=item_id)
        item.delete()
        return redirect('ver_carrito') 


#vista de la pag ayuda
def ayuda(request):
    context= {}
    return render(request, 'animales/ayuda.html', context)

#vista de la pag informacion
def informacion(request):
    context= {}
    return render(request, 'animales/informacion.html', context)


#vista de la pag quienes somos
def QuienesSomos(request):
    context= {}
    return render(request, 'animales/QuienesSomos.html', context)

#vista de la pag productosPerro
def productoPerro(request):
    productos =  ProductoPerros.objects.all()
    return render(request, 'animales/productosPerro.html', {'productos': productos})

#vista de la pag productoGato
def productoGato(request):
    productos =  ProductoGatos.objects.all()
    return render(request, 'animales/productosGato.html', {'productos': productos})





#autenticarse
def acceder(request):
    if request.method == 'GET':
        return render(request, 'animales/inicioDeSesion.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        
        if user is None:
            return render(request, 'animales/inicioDeSesion.html', {'form': AuthenticationForm, 'error': 'Usuario o contraseña es incorrecta'})
        else:
            login(request, user)
            return redirect('lista_productos')
        
        
#registrarse

def signup(request):
    if request.method == 'GET':
        return render(request, 'animales/registro.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except:
                return render(request, 'animales/registro.html', {'form': UserCreationForm, 'error': 'Usuario ya existe'})
        return render(request, 'animales/registro.html', {'form': UserCreationForm, 'error': 'Contraseñas no coinciden'})
            

#cerrar sesion
def salir(request):
    logout(request)
    messages.success(request, F"Tu sesión se ha cerrado correctamente")
    return redirect("inicioDeSesion")

#vista para listar productos desde el admin
# Vista para listar todos los productos (AnimalProducto, ProductoPerros, ProductoGatos)
def lista_productos(request):
    productos_general = AnimalProducto.objects.all()
    productos_perros = ProductoPerros.objects.all()
    productos_gatos = ProductoGatos.objects.all()
    return render(request, 'animales/admin.html', {
        'productos_general': productos_general,
        'productos_perros': productos_perros,
        'productos_gatos': productos_gatos,
    })

#vista para agregar productos desde el admin
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'animales/admin_agregar_producto.html', {'form': form})

# Vista para agregar un producto de perros (ProductoPerros)
def agregar_producto_perros(request):
    if request.method == 'POST':
        form = ProductoPerrosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoPerrosForm()
    return render(request, 'animales/admin_agregar_producto_perros.html', {'form': form})

# Vista para agregar un producto de gatos (ProductoGatos)
def agregar_producto_gatos(request):
    if request.method == 'POST':
        form = ProductoGatosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoGatosForm()
    return render(request, 'animales/admin_agregar_producto_gatos.html', {'form': form})



#vista para editar los productos desde el admin
def editar_producto(request, producto_id):
    producto = get_object_or_404(AnimalProducto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'animales/admin_editar_producto.html', {'form': form, 'producto': producto})

# Vista para editar un producto de perros (ProductoPerros)
def editar_producto_perros(request, producto_id):
    producto = get_object_or_404(ProductoPerros, id=producto_id)
    if request.method == 'POST':
        form = ProductoPerrosForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoPerrosForm(instance=producto)
    return render(request, 'animales/admin_editar_producto_perros.html', {'form': form, 'producto': producto})

# Vista para editar un producto de gatos (ProductoGatos)
def editar_producto_gatos(request, producto_id):
    producto = get_object_or_404(ProductoGatos, id=producto_id)
    if request.method == 'POST':
        form = ProductoGatosForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoGatosForm(instance=producto)
    return render(request, 'animales/admin_editar_producto_gatos.html', {'form': form, 'producto': producto})


#vista para eliminar los productos desde el admin
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(AnimalProducto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'animales/admin_eliminar_producto.html', {'producto': producto})


# Vista para eliminar un producto de perros (ProductoPerros)
def eliminar_producto_perros(request, producto_id):
    producto = get_object_or_404(ProductoPerros, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'animales/admin_eliminar_producto_perros.html', {'producto': producto})

# Vista para eliminar un producto de gatos (ProductoGatos)
def eliminar_producto_gatos(request, producto_id):
    producto = get_object_or_404(ProductoGatos, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'animales/admin_eliminar_producto_gatos.html', {'producto': producto})


#vista para proceder con la compra
def comprar_carrito(request):
    carrito_items = Carrito.objects.all()

    if request.method == 'POST' and carrito_items.exists():
        # Crear un nuevo pedido
        nuevo_pedido = Pedido.objects.create(total=0)
        total = 0

        # Agregar los productos del carrito al pedido
        for item in carrito_items:
            precio_unitario = None
            if item.producto:
                precio_unitario = float(item.producto.precio)
            elif item.producto_perros:
                precio_unitario = float(item.producto_perros.precio)
            elif item.producto_gatos:
                precio_unitario = float(item.producto_gatos.precio)

            PedidoItem.objects.create(
                pedido=nuevo_pedido,
                producto=item.producto,
                producto_perros=item.producto_perros,
                producto_gatos=item.producto_gatos,
                cantidad=item.cantidad,
                precio_unitario=precio_unitario
            )
            total += precio_unitario * item.cantidad

        nuevo_pedido.total = total
        nuevo_pedido.save()

        # Vaciar el carrito
        carrito_items.delete()

        return redirect('confirmacion_compra', pedido_id=nuevo_pedido.id)
    
    return redirect('ver_carrito')

def confirmacion_compra(request, pedido_id):
    pedido = Pedido.objects.get(id=pedido_id)
    for item in pedido.items.all():
        if item.producto:
            item.subtotal = item.cantidad * item.producto.precio
        elif item.producto_perros:
            item.subtotal = item.cantidad * item.producto_perros.precio
        elif item.producto_gatos:
            item.subtotal = item.cantidad * item.producto_gatos.precio

    return render(request, 'animales/confirmacion_compra.html', {'pedido': pedido})