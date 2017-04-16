# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 21:46
from __future__ import unicode_literals

import books.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('autor', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('likes', models.PositiveIntegerField(default=0)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('files', models.FileField(upload_to=books.models.upload_location, validators=[books.models.validate_file_extension])),
                ('book_type', models.CharField(choices=[('Programacion', 'Programacion'), ('Base de Datos', 'Base de Datos'), ('Inteligencia Artificial', 'Inteligencia Artificial'), ('Machine Learning', 'Machine Learning')], max_length=100)),
            ],
        ),
    ]
