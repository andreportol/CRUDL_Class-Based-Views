from django.db import models

# Create your models here.

class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Localizacao(Base):
    inscricao = models.CharField('Inscrição Imobiliária', max_length=11, blank=True, help_text='Digite os 11 números')
    utmX = models.DecimalField('UTM_X', max_digits=8, decimal_places=2, blank=True, null=True)
    utmY = models.DecimalField('UTM_Y', max_digits=8, decimal_places=2, blank=True, null=True)
    REGIAO_CHOICES = (
        ('Anhanduizinho', 'Anhanduizinho'),
        ('Bandeira', 'Bandeira'),
        ('Centro', 'Centro'),
        ('Imbirussu', 'Imbirussu'),
        ('Lagoa', 'Lagoa'),
        ('Prosa', 'Prosa'),
        ('Segredo', 'Segredo'),
        ('Dist_Anhandui', 'Dist. Anhandui'),
        ('Dist_Rochedinho', 'Dist. Rochedinho'),
        ('Zona_Rural', 'Zona Rural'),
    ) 
    regiao = models.CharField('Região', max_length=16, choices=REGIAO_CHOICES, blank=False)
    bairro = models.CharField('Bairro', max_length=100, blank=False)
    parcelamento = models.CharField('Parcelamento', max_length=5, blank=False)
    quadra = models.CharField('Quadra', max_length=5, blank=False)
    lote = models.CharField('Lote', max_length=5, blank=False)
    TIPO_CHOICES = (
        ('Avenida', 'Avenida'),
        ('Rua', 'Rua'),
        ('Travessa', 'Travessa'),
        ('Via', 'Via'),
        ('Rodovia', 'Rodovia'),
        ('Estrada', 'Estrada'),
        ('Chacara', 'Chacara'),
    )  
    tipo_logradouro = models.CharField('Tipo Logradouro', max_length=25, choices=TIPO_CHOICES, blank=False)
    logradouro = models.CharField('Logradouro', max_length=100, blank=False)
    numero = models.CharField('Número', max_length=6, blank=True)
    observacao = models.TextField('Observação', blank=True)
    
    def __str__(self):
        return f' Inscrição Imobiliária: {self.inscricao}'
    
    
    class Meta:
        '''
        As verboses names servem para colocar no painel do django/admin os nomes corretos.
        O não uso das verboses names faz com que o django adicione um 's' no nome 
        da classe e apresente no painel do django admin. Ex. Localizacao ficaria Localizacaos 
        '''
        verbose_name = 'Localização'
        verbose_name_plural = 'Localizações'