# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dp_management', '0044_auto_20150820_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasetstreamproperty',
            name='show_filter_field',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
