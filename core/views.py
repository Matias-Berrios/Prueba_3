from django.shortcuts import render, redirect,get_object_or_404
from .models import Producto
from .forms import ProductoForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404


# Create your views here.

def home(request):
    productos = Producto.objects.all()
    datos = {
        'productos': productos
    }
    return render(request, 'core/home.html', datos)

def crearUsuario(request):
    return render(request, 'core/crearUsuario.html')

def bandana(request):
    producto = Producto.objects.filter(categoria='1')
    return render(request, 'core/bandana.html', {"productos":producto})

def correa(request):
    producto = Producto.objects.filter(categoria='3')
    return render(request, 'core/correa.html', {"productos":producto})

def placa(request):
    producto = Producto.objects.filter(categoria='2')
    return render(request, 'core/placa.html', {"productos":producto})

def tienda_lista(request):
    productos = Producto.objects.all()
    datos = {
        'productos': productos
    }
    return render(request, 'core/tienda_lista.html', datos)

def tienda_principal(request):
    
    productos = Producto.objects.all()
    page = request.GET.get('page',1)

    try: 
       paginator = Paginator(productos,4)
       productos = paginator.page(page)
    except:          
        raise Http404

    datos = {
        'entity':productos,
        'paginator':paginator
    }
    return render(request, 'core/tienda_principal.html', datos)

def registros(request):
    datos = {
        'form': ProductoForm()
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos guardados correctamente"
    return render(request, 'core/registros.html', datos)

def modificar_registros(request,id):
    producto = Producto.objects.get(sku=id)
    datos = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificados correctamente"
    return render(request, 'core/modificar_registros.html', datos)

def borrar_del_producto(request, id):
    producto = Producto.objects.get(sku=id)
    producto.delete()
    return redirect(to="home")

