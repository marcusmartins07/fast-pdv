# Generated by Django 5.1.4 on 2024-12-10 14:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('atualizacao', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('ativo', 'Ativo'), ('inativo', 'Inativo')], default='ativo', max_length=10)),
                ('codigo_categoria', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('atualizacao', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('ativo', 'Ativo'), ('inativo', 'Inativo')], default='ativo', max_length=10)),
                ('produto_id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField(blank=True)),
                ('preco_venda', models.DecimalField(decimal_places=2, max_digits=10)),
                ('preco_custo', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('preco_desconto', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('porcentagem_desconto', models.IntegerField(blank=True, null=True)),
                ('codigo_barras', models.CharField(blank=True, max_length=13, unique=True)),
                ('estoque', models.IntegerField(default=0)),
                ('sku', models.CharField(blank=True, max_length=50, unique=True)),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='produto.categoria')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
