# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dp_management', '0036_auto_20150813_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasource',
            name='date_last_update',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 13, 14, 41, 26, 169575), null=True),
            preserve_default=True,
        ),
    ]
