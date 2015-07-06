# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dp_management', '0006_datamodelpivotpoint'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataProject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=56)),
                ('description', models.TextField(null=True, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=56)),
                ('description', models.TextField(null=True, blank=True)),
                ('data_project', models.ForeignKey(to='dp_management.DataProject')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DataSetStream',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_set', models.ForeignKey(to='dp_management.DataSet')),
                ('data_stream', models.ForeignKey(to='dp_management.DataSource')),
            ],
            options={
                'verbose_name': 'Data set stream',
                'verbose_name_plural': 'Data set streams',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DataSetStreamProperty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action', models.IntegerField(default=0, choices=[(0, b'SUM'), (1, b'AVG'), (2, b'MAX'), (3, b'MIN'), (4, b'GROUP BY')])),
                ('filter_value', models.CharField(max_length=512, null=True, blank=True)),
                ('data_model_property', models.ForeignKey(to='dp_management.DataModelProperty')),
                ('data_set_stream', models.ForeignKey(to='dp_management.DataSetStream')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='datamodeledge',
            name='data_source',
            field=models.ForeignKey(default=1, to='dp_management.DataSource'),
            preserve_default=False,
        ),
    ]
