# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-08 17:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Correct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ans', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Answers')),
                ('Ques', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Question')),
            ],
        ),
    ]