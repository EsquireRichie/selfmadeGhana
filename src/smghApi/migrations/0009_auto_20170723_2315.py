# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-23 23:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smghApi', '0008_auto_20170723_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]