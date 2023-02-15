# Generated by Django 4.1.6 on 2023-02-15 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_localizacao_inscricao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localizacao',
            name='numero',
            field=models.CharField(blank=True, max_length=6, verbose_name='Número'),
        ),
        migrations.AlterField(
            model_name='localizacao',
            name='observacao',
            field=models.TextField(blank=True, verbose_name='Observação'),
        ),
    ]