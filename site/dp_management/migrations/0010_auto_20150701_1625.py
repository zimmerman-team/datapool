# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dp_management', '0009_datamodeledge_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datamodeledge',
            name='name',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
    ]
