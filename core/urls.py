from django.urls import path

from .views import (CreateCadastroView, IndexView, ListarDadosView,
                    UpdateCadastroView)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('listardados', ListarDadosView.as_view(), name='listardados'),
    path('dadosComplementares/<int:pk>',ListarDadosView.dadosComplementares, name='dadosComplementares'),
    path('cadastro', CreateCadastroView.as_view(), name='cadastro'),
    path('<int:pk>/update/', UpdateCadastroView.as_view(), name='update_cadastro')
]


