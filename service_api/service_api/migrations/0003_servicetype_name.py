# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 22:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_api', '0002_servicearea_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicetype',
            name='name',
            field=models.CharField(default=None, max_length=256),
            preserve_default=False,
        ),
    ]
