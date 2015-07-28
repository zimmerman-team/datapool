# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dp_management', '0016_auto_20150727_1435'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datasourcecategory',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='datasourcesubcategory',
            options={'verbose_name': 'Sub Category', 'verbose_name_plural': 'Sub Categories'},
        ),
    ]
