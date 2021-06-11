# Generated by Django 3.2.4 on 2021-06-10 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('resumo', models.CharField(default='', max_length=255)),
                ('sexo', models.CharField(choices=[('N', 'Não Informado'), ('M', 'Masculino'), ('F', 'Feminino')], default='N', max_length=1)),
                ('formacao', models.CharField(choices=[('N', 'Não Informado'), ('M', 'Masculino'), ('F', 'Feminino')], default='ND', max_length=2)),
                ('cep', models.CharField(default='', max_length=8)),
                ('email', models.CharField(max_length=100)),
                ('avatar', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]