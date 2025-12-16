from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):

    return render(request, "proyecto_web_app/home.html")


