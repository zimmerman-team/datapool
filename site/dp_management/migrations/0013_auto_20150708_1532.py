# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dp_management', '0012_auto_20150707_1531'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dollydata',
            old_name='longtitude',
            new_name='longitude',
        ),
    ]
