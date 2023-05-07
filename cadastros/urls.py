from django.urls import path
from .views import ClienteCreate, EntregaCreate

urlpatterns = [
    path('cadastrar/cliente/', ClienteCreate.as_view(), name='cadastrar-cliente'),
    path('cadastrar/entrega/', EntregaCreate.as_view(), name='cadastrar-entrega'),
]
