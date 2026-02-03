from django.shortcuts import render, HttpResponse

from carro.carro import Carro


# Create your views here.
def home(request):
    carro = Carro(request)
    return render(request, "proyecto_web_app/home.html")


