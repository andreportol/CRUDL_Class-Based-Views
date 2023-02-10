import django_filters

from .models import Localizacao


class CadastroFilter(django_filters.FilterSet):
    inscricao = django_filters.CharFilter(lookup_expr='icontains')
    #regiao = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Localizacao
        fields = ('inscricao',) 