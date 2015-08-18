# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dp_management', '0039_auto_20150817_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasource',
            name='date_last_update',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 18, 10, 5, 43, 398915), null=True),
            preserve_default=True,
        ),
    ]
