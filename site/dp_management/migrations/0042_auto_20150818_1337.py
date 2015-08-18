# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dp_management', '0041_auto_20150818_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataModelRegexp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('script', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='datamodelproperty',
            name='regexp',
            field=models.ManyToManyField(to='dp_management.DataModelRegexp', null=True, blank=True),
            preserve_default=True,
        ),
    ]
