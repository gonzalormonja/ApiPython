# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-09 00:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TpPythonApp', '0013_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(default='', max_length=2000),
        ),
    ]
