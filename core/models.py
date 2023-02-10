from django.db import models

# Create your models here.

class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Localizacao(Base):
    inscricao = models.CharField('Inscrição Imobiliária', max_length=11, null=None)
    utmX = models.DecimalField('UTM_X', max_digits=8, decimal_places=2, null=None)
    utmY = models.DecimalField('UTM_Y', max_digits=8, decimal_places=2, null=None)
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
    regiao = models.CharField('Região', max_length=16, choices=REGIAO_CHOICES)
    bairro = models.CharField('Bairro', max_length=100)
    parcelamento = models.CharField('Parcelamento', max_length=5)
    quadra = models.CharField('Quadra', max_length=5)
    lote = models.CharField('Lote', max_length=5)
    TIPO_CHOICES = (
        ('Avenida', 'Avenida'),
        ('Rua', 'Rua'),
        ('Travessa', 'Travessa'),
        ('Via', 'Via'),
        ('Rodovia', 'Rodovia'),
        ('Estrada', 'Estrada'),
        ('Chacara', 'Chacara'),
    )  
    tipo_logradouro = models.CharField('Tipo Logradouro', max_length=25, choices=TIPO_CHOICES)
    logradouro = models.CharField('Logradouro', max_length=100)
    numero = models.CharField('Número', max_length=6)
    observacao = models.TextField('Observação', null=None)
    
    def __str__(self):
        return f' Inscrição Imobiliária: {self.inscricao}'
        