# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dp_management', '0022_auto_20150804_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasetstreamproperty',
            name='action',
            field=models.IntegerField(default=0, choices=[(0, b'SELECT'), (1, b'SEARCHBOX'), (2, b'BETWEEN'), (3, b'MIN'), (4, b'MAX'), (5, b'SUM'), (6, b'AVG'), (7, b'FILTER'), (8, b'COUNT')]),
            preserve_default=True,
        ),
    ]
