# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-15 01:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('email', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('position', models.CharField(max_length=200)),
                ('hireDate', models.DateField(blank=True, default=datetime.date(2018, 2, 15))),
                ('experience', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Employees',
        ),
    ]
