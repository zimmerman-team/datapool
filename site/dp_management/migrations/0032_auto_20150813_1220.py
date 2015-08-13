# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dp_management', '0031_auto_20150813_1118'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataModelScript',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('return_values', models.TextField()),
                ('script', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='datamodelproperty',
            name='unpacking_script',
        ),
        migrations.RemoveField(
            model_name='datasource',
            name='data_from_date',
        ),
        migrations.RemoveField(
            model_name='datasource',
            name='data_to_date',
        ),
        migrations.AddField(
            model_name='datamodelproperty',
            name='script',
            field=models.ForeignKey(to='dp_management.DataModelScript', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='datasource',
            name='date_last_update',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 13, 12, 20, 45, 314204), null=True),
            preserve_default=True,
        ),
    ]
