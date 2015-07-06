# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dp_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datamodelquery',
            name='data_source',
            field=models.ForeignKey(default=12, to='dp_management.DataSource'),
            preserve_default=False,
        ),
    ]
