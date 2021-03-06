# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-09 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(default='\u9673\u66c9\u8587', max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('star', models.CharField(max_length=10)),
                ('height', models.CharField(default='165', max_length=10)),
                ('hair', models.CharField(max_length=50)),
                ('eye', models.CharField(max_length=50)),
                ('political', models.CharField(max_length=50)),
                ('job', models.CharField(max_length=50)),
                ('income', models.CharField(max_length=100)),
                ('relationship', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=50)),
                ('education', models.CharField(max_length=50)),
                ('sport_habbit', models.CharField(max_length=50)),
                ('want_child', models.CharField(max_length=50)),
                ('children', models.CharField(max_length=50)),
                ('figure', models.CharField(max_length=50)),
                ('faith', models.CharField(max_length=50)),
                ('smoke', models.CharField(max_length=50)),
                ('drink', models.CharField(max_length=50)),
                ('checkbox_value', models.CharField(default='A', max_length=250)),
            ],
        ),
    ]
