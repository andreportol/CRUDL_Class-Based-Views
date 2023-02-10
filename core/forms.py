from django import forms

from .models import Localizacao


class LocalizacaoModelForm(forms.ModelForm):

    class Meta:
        model = Localizacao
        fields = '__all__'