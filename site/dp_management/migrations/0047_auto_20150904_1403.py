# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dp_management', '0046_auto_20150903_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataproject',
            name='sub_title',
            field=models.CharField(max_length=56, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='datasetstream',
            name='data_project',
            field=models.ForeignKey(related_name='data_streams', to='dp_management.DataProject'),
            preserve_default=True,
        ),
    ]
