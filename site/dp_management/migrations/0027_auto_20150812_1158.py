# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dp_management', '0026_auto_20150812_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datamodelclass',
            name='translated_name',
            field=models.CharField(max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
    ]
