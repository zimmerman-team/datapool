# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dp_management', '0013_auto_20150708_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataconnection',
            name='host',
            field=models.GenericIPAddressField(),
            preserve_default=True,
        ),
    ]
