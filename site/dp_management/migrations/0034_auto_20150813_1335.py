# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dp_management', '0033_auto_20150813_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasource',
            name='data_file',
            field=models.FileField(null=True, upload_to=b'data_files', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='datasource',
            name='date_last_update',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 13, 13, 35, 21, 664400), null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='datasource',
            name='url',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
