# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-15 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_starlist_star_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchlist',
            name='star',
            field=models.CharField(default='\u694a\u7950\u5be7', max_length=50),
        ),
        migrations.AlterField(
            model_name='registration',
            name='matchgender',
            field=models.CharField(default='\u7537', max_length=50),
        ),
    ]
