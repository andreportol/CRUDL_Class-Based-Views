# Generated by Django 4.1.6 on 2023-02-13 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_localizacao_inscricao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localizacao',
            name='regiao',
            field=models.CharField(choices=[('Anhanduizinho', 'Anhanduizinho'), ('Bandeira', 'Bandeira'), ('Centro', 'Centro'), ('Imbirussu', 'Imbirussu'), ('Lagoa', 'Lagoa'), ('Prosa', 'Prosa'), ('Segredo', 'Segredo'), ('Dist_Anhandui', 'Dist. Anhandui'), ('Dist_Rochedinho', 'Dist. Rochedinho'), ('Zona_Rural', 'Zona Rural')], max_length=16, verbose_name='Região'),
        ),
    ]
