# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 16:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0008_auto_20170205_0703'),
    ]

    operations = [
        migrations.CreateModel(
            name='compilerquestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('code', models.TextField()),
            ],
        ),
    ]