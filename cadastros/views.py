from django.views.generic.edit import CreateView
from .models import Cliente
from django.urls import reverse_lazy

# Create your views here.

class ClienteCreate(CreateView):
    model = Cliente
    fields = ['nome', 'cpf', 'telefone', 'endereco']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')


