# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dp_management', '0049_datasource_scan_dir'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datamodelclass',
            name='name',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
    ]
