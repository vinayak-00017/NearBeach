# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 11:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NearBeach', '0010_customers_organisation_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customers',
            old_name='organisation_id',
            new_name='organisations_id',
        ),
    ]