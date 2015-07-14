# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dp_management', '0014_auto_20150710_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataconnection',
            name='password',
            field=models.CharField(max_length=512),
            preserve_default=True,
        ),
    ]
