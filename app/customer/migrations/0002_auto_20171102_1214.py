# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 12:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer_customerinfo',
            old_name='customer_name',
            new_name='name',
        ),
    ]
