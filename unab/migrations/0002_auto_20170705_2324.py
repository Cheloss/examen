# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-05 23:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unab', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactos',
            name='telefono',
            field=models.CharField(max_length=60),
        ),
    ]
