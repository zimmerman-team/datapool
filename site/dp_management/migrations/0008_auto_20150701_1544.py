# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dp_management', '0007_auto_20150701_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datamodelproperty',
            name='data_model_subgroup',
            field=models.ForeignKey(to='dp_management.DataModelSubGroup', null=True),
            preserve_default=True,
        ),
    ]
