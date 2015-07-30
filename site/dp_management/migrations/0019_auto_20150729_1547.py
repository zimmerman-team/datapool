# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dp_management', '0018_auto_20150729_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datasetstream',
            name='data_project',
        ),
        migrations.AddField(
            model_name='dataproject',
            name='data_streams',
            field=models.ManyToManyField(to='dp_management.DataSetStream', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='datasetstream',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
