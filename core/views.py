from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .filters import CadastroFilter
from .models import Localizacao


# abrir o template principal
class IndexView(TemplateView):
    template_name = "index.html"
    
# Lista os dados     
class ListarDadosView(ListView):
    models = Localizacao
    template_name = 'listardados.html'
    queryset = Localizacao.objects.order_by('id').all() # Retorna todos os registros do banco de dados ordenados por "id".
    context_object_name = 'localizacao' # nome para acessar no template
    
    def dadosComplementares(request, pk):
        context = {
            'complementos' : Localizacao.objects.filter(id = pk)
        }
        return render(request, 'dadosComplementares.html', context)


class CreateCadastroView(CreateView):
    model = Localizacao
    template_name = 'cadastro.html'
    fields = ['inscricao', 'utmX', 'utmY','regiao', 'bairro', 'parcelamento', 'quadra',
        'lote','tipo_logradouro','logradouro','numero', 'observacao']
    success_url = reverse_lazy('cadastro') # local que será redirecionado em caso de sucesso, o nome cadastra está na urls.py
    
    
class UpdateCadastroView(UpdateView):
    model = Localizacao
    template_name = 'cadastro.html'
    fields = ['inscricao', 'utmX', 'utmY','regiao', 'bairro', 'parcelamento', 'quadra',
        'lote','tipo_logradouro','logradouro','numero', 'observacao',]
    queryset = Localizacao.objects.order_by('id').all()
    context_object_name = 'localizacao'
    success_url = reverse_lazy('listardados')


class DeleteCadastroView(DeleteView):
    model = Localizacao
    template_name = 'cadastro_del.html'
    success_url = reverse_lazy('listardados')  

class PesquisaCadastro():
    
    def pesquisar(request):
        template_name = 'pesquisaCadastro.html'
        object_list = Localizacao.objects.all()
        cadastro_list = CadastroFilter(request.GET, queryset=object_list)
        context = {
            'object_list' : object_list,
            'filter': cadastro_list
        }
        return render(request, template_name, context)
