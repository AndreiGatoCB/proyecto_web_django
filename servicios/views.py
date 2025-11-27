from django.shortcuts import render
from servicios.models import Servicio

# Create your views here.


def servicios(request):

    servicios_ = Servicio.objects.all()
    return render(request, "servicios/servicios.html", {"servicios": servicios_})

