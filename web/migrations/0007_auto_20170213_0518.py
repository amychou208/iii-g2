# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-13 05:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_choose_starlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='want_child',
            new_name='wantchild',
        ),
    ]
