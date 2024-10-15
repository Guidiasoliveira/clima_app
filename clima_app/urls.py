from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  # Importa a view para redirecionar

urlpatterns = [
    path('', RedirectView.as_view(url='/clima/')),  # Redireciona a URL base para /clima/
    path('admin/', admin.site.urls),
    path('clima/', include('clima.urls')),
]
