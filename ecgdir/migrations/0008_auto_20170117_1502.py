# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecgdir', '0007_organization_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='contact_email',
            field=models.EmailField(max_length=254, verbose_name='email de contacto'),
        ),
    ]
