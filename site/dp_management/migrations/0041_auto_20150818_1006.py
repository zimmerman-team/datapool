# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dp_management', '0040_auto_20150818_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasource',
            name='date_last_update',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
