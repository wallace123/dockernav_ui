# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 12:07
from __future__ import unicode_literals

from django.db import migrations, models
import dockernav.models


class Migration(migrations.Migration):

    dependencies = [
        ('dockernav', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='container',
            name='directory',
            field=models.CharField(default=dockernav.models.make_dir, max_length=30),
        ),
    ]