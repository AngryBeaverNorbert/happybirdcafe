# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 19:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('phone', models.CharField(max_length=200, verbose_name='phone')),
                ('email', models.CharField(max_length=200, verbose_name='e-mail')),
                ('text', models.TextField(verbose_name='text')),
                ('image', models.ImageField(blank=True, null=True, upload_to='contacts/%Y/%m/%d', verbose_name='image')),
                ('created_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='created date')),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='published date')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='author')),
            ],
            options={
                'ordering': ('title',),
                'verbose_name': 'contacts',
                'verbose_name_plural': 'contacts',
            },
        ),
    ]
