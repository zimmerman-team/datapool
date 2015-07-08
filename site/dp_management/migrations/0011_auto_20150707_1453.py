# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dp_management', '0010_auto_20150701_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='DollyData',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('latitude', models.FloatField()),
                ('longtitude', models.FloatField()),
                ('create_at', models.DateTimeField()),
                ('text', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keyword', models.CharField(max_length=128, null=True, blank=True)),
                ('count', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TwitterUser',
            fields=[
                ('u_id', models.IntegerField(serialize=False, primary_key=True)),
                ('count', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='dollydata',
            name='u_id',
            field=models.ForeignKey(to='dp_management.TwitterUser'),
            preserve_default=True,
        ),
    ]
