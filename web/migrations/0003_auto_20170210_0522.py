# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-10 05:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_registration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='checkbox_value',
        ),
        migrations.AddField(
            model_name='registration',
            name='interest',
            field=models.CharField(default='[\u5916\u51fa\u5c31\u9910,\u97f3\u6a02\u8207\u97f3\u6a02\u6703,\u65c5\u904a/\u89c0\u5149,\u559d\u5496\u5561\u804a\u5929,\u96fb\u5f71/\u8996\u983b]', max_length=250),
        ),
        migrations.AddField(
            model_name='registration',
            name='race',
            field=models.CharField(default='\u4e9e\u6d32\u4eba', max_length=250),
        ),
        migrations.AddField(
            model_name='registration',
            name='sport',
            field=models.CharField(default='[\u9a0e\u8173\u8e0f\u8eca,\u649e\u7403/\u684c\u7403,\u4fdd\u9f61\u7403,\u6563\u6b65]', max_length=250),
        ),
    ]