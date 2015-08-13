# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dp_management', '0028_remove_datamodelgroup_data_model_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='datamodelclass',
            name='orient_name',
            field=models.CharField(max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
    ]
