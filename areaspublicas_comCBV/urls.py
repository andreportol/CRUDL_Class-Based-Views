
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),   
] 

# Alterando o painel administrativo do Django (HÁ OUTRAS DUAS FORMAS)
admin.AdminSite.site_header = 'Sistema Semadur'
admin.AdminSite.index_title = 'ALP_SOFTWARES'
admin.AdminSite.site_title = 'Áreas Públicas'

'''
Outra maneira de alterar o painel administrativo do django é:
1) Instalando o django-adminlte2 -> pip install django-adminlte2
2) Em INSTALLED_APPS do settings.py adicionar django_adminlte e django_adminlte_theme
    obs. Instalar nas primeiras posições do INSTALLED_APPS para sobrescrever as demais
'''

'''
OUTRA MANEIRA:
 1) Instalando o django-adminlte2 -> pip install django-adminlte2
 2) Em INSTALLED_APPS do settings.py adicionar django_adminlte e django_adminlte_theme
    obs. Instalar nas primeiras posições do INSTALLED_APPS para sobrescrever as demais
 3) Criar uma pasta 'templates' na raiz do projeto;
 4) Copiar as pastas django_adminlte e django_adminlte_theme para pasta templates
    .venv\Lib\site-packages\django_adminlte\templates\adminlte
    .venv\Lib\site-packages\django_adminlte_theme\templates\admin

    
'''