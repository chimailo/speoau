# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2006-07-06 23:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_member_dept'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='dept',
            field=models.CharField(choices=[('age', 'Agricultural Engineering'), ('che', 'Chemical Engineering'), ('chm', 'Chemistry'), ('cve', 'Civil Engineering'), ('csc', 'Computer Engineering'), ('eee', 'Elect. Elect. Engineering'), ('geo', 'Geology'), ('msc', 'Materials Science Engineering'), ('mth', 'Mathematics'), ('mee', 'Mechanical Engineering'), ('phy', 'Physics')], max_length=3, verbose_name='Department'),
        ),
    ]
