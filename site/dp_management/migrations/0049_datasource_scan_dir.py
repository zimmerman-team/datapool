# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dp_management', '0048_auto_20150909_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasource',
            name='scan_dir',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
