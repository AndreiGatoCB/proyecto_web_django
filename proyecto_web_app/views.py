from django.shortcuts import render, HttpResponse
from servicios.models import Servicio


# Create your views here.
def home(request):

    return render(request, "proyecto_web_app/home.html")


def servicios(request):

    servicios_ = Servicio.objects.all()
    return render(request, "proyecto_web_app/servicios.html", {"servicios": servicios_})


def tienda(request):

    return render(request, "proyecto_web_app/tienda.html")


def blog(request):

    return render(request, "proyecto_web_app/blog.html")


def contacto(request):

    return render(request, "proyecto_web_app/contacto.html")
