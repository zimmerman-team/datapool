# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dp_management', '0027_auto_20150812_1158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datamodelgroup',
            name='data_model_class',
        ),
    ]
