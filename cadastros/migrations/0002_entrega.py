# Generated by Django 4.2 on 2023-05-07 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=250, verbose_name='endereço')),
                ('caixas', models.IntegerField()),
                ('volumeextra', models.CharField(max_length=150, verbose_name='Volume Extra')),
                ('nomeembalador', models.CharField(max_length=50, verbose_name='Nome do Embalador')),
                ('datacompra', models.DateField(blank=True, null=True, verbose_name='data')),
                ('datahoraentrega', models.DateTimeField(blank=True, null=True, verbose_name='data')),
            ],
        ),
    ]