# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 07:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0004_auto_20170730_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boards.thread'),
        ),
    ]