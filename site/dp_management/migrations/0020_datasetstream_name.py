# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dp_management', '0019_auto_20150729_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasetstream',
            name='name',
            field=models.CharField(default='dataset name', max_length=56),
            preserve_default=False,
        ),
    ]
