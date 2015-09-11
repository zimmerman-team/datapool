# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dp_management', '0047_auto_20150904_1403'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datasetstream',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='datasetstream',
            name='extra_where_clause',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
