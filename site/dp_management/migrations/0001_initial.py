# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DataConnection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('host', models.URLField()),
                ('port', models.IntegerField(default=2424)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DataModelClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('default_cluster_id', models.CharField(max_length=5)),
                ('translated_name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DataModelEdge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('class_in', models.ForeignKey(related_name='class_in', to='dp_management.DataModelClass')),
                ('class_out', models.ForeignKey(related_name='class_out', to='dp_management.DataModelClass')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DataModelEdgeProperty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('property_type', models.CharField(max_length=30)),
                ('data_model_edge', models.ForeignKey(to='dp_management.DataModelEdge')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DataModelGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('data_model_class', models.ForeignKey(to='dp_management.DataModelClass')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DataModelProperty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('translated_name', models.CharField(max_length=30)),
                ('property_type', models.CharField(max_length=30)),
                ('property_values', models.TextField()),
                ('data_model_class', models.ForeignKey(to='dp_management.DataModelClass')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DataModelQuery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(editable=False, db_index=True)),
                ('name', models.CharField(max_length=30)),
                ('query', models.TextField()),
                ('run_after_update', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
                'verbose_name': 'DataModel Query',
                'verbose_name_plural': 'DataModel Queries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DataModelSubGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('data_model_group', models.ForeignKey(to='dp_management.DataModelGroup')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DataSource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('url', models.URLField()),
                ('prefix', models.CharField(max_length=10)),
                ('private', models.BooleanField(default=False)),
                ('data_type', models.IntegerField(default=0, choices=[(0, b'CSV'), (1, b'XML'), (2, b'JSON')])),
                ('old_data_choice', models.IntegerField(default=0, choices=[(0, b'REMOVE'), (1, b'APPEND'), (2, b'OVERWRITE')])),
                ('csv_seprator', models.CharField(max_length=5)),
                ('new_row_on_number', models.BooleanField(default=False)),
                ('new_row_on_number_name', models.CharField(max_length=30)),
                ('overwrite_fields', models.CharField(max_length=50)),
                ('data_from_date', models.DateTimeField(null=True)),
                ('data_to_date', models.DateTimeField(null=True)),
                ('quality_of_source', models.FloatField(default=5.0)),
                ('data_connection', models.ForeignKey(to='dp_management.DataConnection')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DataSourceComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField()),
                ('data_source', models.ForeignKey(to='dp_management.DataSource')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DataSourceFlags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='datasource',
            name='flags',
            field=models.ManyToManyField(to='dp_management.DataSourceFlags'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='datasource',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='datamodelproperty',
            name='data_model_subgroup',
            field=models.ForeignKey(to='dp_management.DataModelSubGroup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='datamodelclass',
            name='data_source',
            field=models.ForeignKey(to='dp_management.DataSource'),
            preserve_default=True,
        ),
    ]
