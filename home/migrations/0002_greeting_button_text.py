# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-13 20:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='greeting',
            name='button_text',
            field=models.CharField(default='', max_length=20, verbose_name='button text'),
            preserve_default=False,
        ),
    ]
