# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-10 05:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20170210_0522'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='matchgender',
            field=models.CharField(default='\u7537', max_length=10),
        ),
        migrations.AddField(
            model_name='registration',
            name='tag',
            field=models.CharField(default='[\u6797\u4f9d\u6668]', max_length=250),
        ),
    ]