# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dp_management', '0004_auto_20150629_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasource',
            name='date_last_update',
            field=models.DateTimeField(default=None, null=True),
            preserve_default=True,
        ),
    ]
