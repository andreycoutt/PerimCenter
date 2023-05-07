from django.urls import path
from .views import ClienteCreate

urlpatterns = [
    path('cadastrar/cliente/', ClienteCreate.as_view(), name='cadastrar-cliente'),
]
