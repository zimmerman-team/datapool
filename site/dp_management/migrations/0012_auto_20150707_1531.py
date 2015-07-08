# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dp_management', '0011_auto_20150707_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dollydata',
            name='id',
            field=models.BigIntegerField(serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='twitteruser',
            name='u_id',
            field=models.BigIntegerField(serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
