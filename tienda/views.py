from django.shortcuts import render
from tienda.models import Producto

# Create your views here.


def tienda(request):
    tienda_ = Producto.objects.all()
    return render(request, "tienda/tienda.html", {"tienda": tienda_})


def producto(request, producto_id):
    producto = Producto.object.get(id=producto_id)
    return render(request, "tienda/tienda.html", {"producto": producto})
