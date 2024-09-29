from django.shortcuts import get_object_or_404, render
from tienda.models import Producto, Categoria

def index(request):
    product_list = Producto.objects.order_by('nombre')[:6] 
    category_list = Categoria.objects.all() 
    context = {
        'product_list': product_list,
        'category_list': category_list
    }
    return render(request, 'index.html', context)

def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    category_list = Categoria.objects.all()
    return render(request, 'producto.html', {'producto': producto, 'category_list': category_list})

def productos_p(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    productos = Producto.objects.filter(categoria=categoria)
    category_list = Categoria.objects.all()
    context = {
        'productos': productos,
        'categoria': categoria,
        'category_list': category_list
    }
    return render(request, 'productos_categoria.html', context)
