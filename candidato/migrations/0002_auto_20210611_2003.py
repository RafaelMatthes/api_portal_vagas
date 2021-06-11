# Generated by Django 3.2.4 on 2021-06-11 23:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('candidato', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidato',
            name='data_cadastro',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='formacao',
            field=models.CharField(choices=[('ND', 'Não Informado'), ('EB', 'Ensino Básico'), ('EM', 'Ensino Médio'), ('ES', 'Ensino Superior')], default='ND', max_length=2),
        ),
    ]