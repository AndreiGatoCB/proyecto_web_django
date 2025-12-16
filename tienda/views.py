from django.shortcuts import render
from tienda.models import Tienda

# Create your views here.


def tienda(request):
    # tienda_ = Tienda.objects.all()
    return render(request, "tienda/tienda.html")#, #{"tienda": tienda_})
