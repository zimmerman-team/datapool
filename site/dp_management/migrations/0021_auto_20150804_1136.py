# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dp_management', '0020_datasetstream_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasetstreamproperty',
            name='data_stream_class',
            field=models.ForeignKey(default=1, to='dp_management.DataModelClass'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='datamodelclass',
            name='data_source',
            field=models.ForeignKey(related_name='classes', to='dp_management.DataSource'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='datamodelproperty',
            name='data_model_class',
            field=models.ForeignKey(related_name='properties', to='dp_management.DataModelClass'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='datasetstream',
            name='data_stream',
            field=models.ForeignKey(related_name='data_set_streams', to='dp_management.DataSource'),
            preserve_default=True,
        ),
    ]
