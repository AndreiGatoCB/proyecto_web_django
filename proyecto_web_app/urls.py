from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from proyecto_web_app import views


urlpatterns = [
    path('', views.home, name="Home"),
]

urlpatterns += (static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
