# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-08 13:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Answer', models.CharField(max_length=220)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=220)),
            ],
        ),
        migrations.AddField(
            model_name='answers',
            name='Question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Question'),
        ),
    ]
