from django.contrib import admin

from .models import Localizacao


@admin.register(Localizacao)
class LocalizacaoAdmin(admin.ModelAdmin):
    list_display = ('inscricao','utmX', 'utmY','regiao', 'bairro', 'numero', 'observacao')
