# Generated by Django 5.1.4 on 2024-12-10 14:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('atualizacao', models.DateTimeField(auto_now=True)),
                ('ativo', models.BooleanField(default=True)),
                ('uf', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('estado', models.CharField(max_length=55, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('atualizacao', models.DateTimeField(auto_now=True)),
                ('ativo', models.BooleanField(default=True)),
                ('id_genero', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('genero', models.CharField(max_length=55, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('atualizacao', models.DateTimeField(auto_now=True)),
                ('ativo', models.BooleanField(default=True)),
                ('cliente_id', models.AutoField(primary_key=True, serialize=False)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('nome', models.CharField(max_length=255)),
                ('data_nascimento', models.DateField()),
                ('cep', models.CharField(max_length=8)),
                ('endereco', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=6)),
                ('bairro', models.CharField(max_length=55)),
                ('cidade', models.CharField(max_length=55)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('tel_celular', models.CharField(max_length=12)),
                ('uf_estado', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='usuarios.estado')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='usuarios.genero')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['cliente_id'],
                'unique_together': {('cpf',)},
            },
        ),
    ]
