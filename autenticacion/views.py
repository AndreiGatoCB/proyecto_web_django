from django.shortcuts import render
from autenticacion.models import Autenticacion
# Create your views here.


def autenticacion(request):
    autenticacion_ = Autenticacion.objects.all()
    return render(request, "registro/registro.html", {"productos": autenticacion_})
