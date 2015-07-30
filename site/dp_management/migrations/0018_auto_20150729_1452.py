# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dp_management', '0017_auto_20150727_1708'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataset',
            name='data_project',
        ),
        migrations.RemoveField(
            model_name='datasetstream',
            name='data_set',
        ),
        migrations.DeleteModel(
            name='DataSet',
        ),
        migrations.AddField(
            model_name='datasetstream',
            name='data_project',
            field=models.ForeignKey(default=1, to='dp_management.DataProject'),
            preserve_default=False,
        ),
    ]
