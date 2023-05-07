from django.views.generic.edit import CreateView
from .models import Cliente, Entrega
from django.urls import reverse_lazy

# Create your views here.

class ClienteCreate(CreateView):
    model = Cliente
    fields = ['nome', 'cpf', 'telefone', 'endereco']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')

class EntregaCreate(CreateView):
    model = Entrega
    fields = ['nome', 'endereco', 'caixas', 'volumeextra', 'nomeembalador', 'datacompra', 'datahoraentrega']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')

