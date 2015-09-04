# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dp_management', '0045_datasetstreamproperty_show_filter_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataproject',
            name='data_streams',
        ),
        migrations.AddField(
            model_name='datasetstream',
            name='data_project',
            field=models.ForeignKey(default=26, to='dp_management.DataProject'),
            preserve_default=False,
        ),
    ]
