# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dp_management', '0024_auto_20150806_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='datamodelproperty',
            name='orient_name',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
