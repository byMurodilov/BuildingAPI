# Generated by Django 5.0.6 on 2024-06-01 08:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hudud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=110, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Qurilishtashkiloti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('qachon_ttopgan', models.IntegerField()),
                ('hudud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Builting.hudud')),
            ],
        ),
        migrations.CreateModel(
            name='Qurilishbinosi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, unique=True)),
                ('maydoni_kv', models.IntegerField()),
                ('qavat', models.IntegerField()),
                ('parkovkasi', models.BooleanField(default=False)),
                ('kindergarden', models.BooleanField(default=False)),
                ('lift', models.BooleanField(default=True)),
                ('hudud_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Builting.hudud')),
                ('qurilishtashkiloti', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Builting.qurilishtashkiloti')),
            ],
        ),
    ]
