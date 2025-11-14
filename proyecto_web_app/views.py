from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):

    return render(request, "proyecto_web_app/home.html")


def servicios(request):

    return render(request, "proyecto_web_app/servicios.html")


def tienda(request):

    return render(request, "proyecto_web_app/tienda.html")


def blog(request):

    return render(request, "proyecto_web_app/blog.html")


def contacto(request):

    return render(request, "proyecto_web_app/contacto.html")
