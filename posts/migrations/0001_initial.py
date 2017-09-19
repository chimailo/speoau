# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50, verbose_name='Full Name')),
                ('office', models.CharField(max_length=50, verbose_name='Post Held')),
                ('matric_no', models.CharField(max_length=12)),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='date published')),
                ('pub_date', models.DateField(blank=True, null=True, verbose_name='date published')),
                ('body', models.TextField()),
            ],
        ),
    ]
