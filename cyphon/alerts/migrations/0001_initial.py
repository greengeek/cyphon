# -*- coding: utf-8 -*-
# Copyright 2017 Dunbar Security Solutions, Inc.
#
# This file is part of Cyphon Engine.
#
# Cyphon Engine is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# Cyphon Engine is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Cyphon Engine. If not, see <http://www.gnu.org/licenses/>.
#
# Generated by Django 1.10.1 on 2017-03-20 16:23
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('CRITICAL', 'Critical'), ('HIGH', 'High'), ('MEDIUM', 'Medium'), ('LOW', 'Low'), ('INFO', 'Info')], db_index=True, max_length=20)),
                ('status', models.CharField(choices=[('NEW', 'New'), ('BUSY', 'Busy'), ('DONE', 'Done')], db_index=True, default='NEW', max_length=20)),
                ('outcome', models.CharField(blank=True, choices=[('false positive', 'false positive'), ('duplicate', 'duplicate'), ('completed', 'completed'), ('N/A', 'N/A')], db_index=True, max_length=20, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('content_date', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, null=True)),
                ('alarm_id', models.PositiveIntegerField(blank=True, null=True)),
                ('doc_id', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('incidents', models.PositiveIntegerField(default=1)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
            options={
                'permissions': (('view_alert', 'Can see existing alerts'),),
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('alert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', related_query_name='comment', to='alerts.Alert')),
            ],
            options={
                'permissions': (('view_alert', 'Can see existing alerts'),),
                'ordering': ['id'],
            },
        ),
    ]