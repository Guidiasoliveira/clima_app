from django.urls import path
from .views import clima_view  # Importa a função clima_view

urlpatterns = [
    path('', clima_view, name='clima'),  # Mapeia a URL base para a função clima_view
]
