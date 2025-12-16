from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage
import credentials


# Create your views here.
def contacto(request):
    formulario_contacto = FormularioContacto
    if request.method == "POST":
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            email_ = EmailMessage("Mensaje desde proyecto web app django",
                                  f"El usuario {nombre} cuyo correo es {email} escribe: \n\n {contenido}",
                                  "", [credentials.EMAIL_HOST_USER], reply_to=[email])
            try:
                email_.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")

    return render(request, "contacto/contacto.html", {'miFormulario': formulario_contacto})
