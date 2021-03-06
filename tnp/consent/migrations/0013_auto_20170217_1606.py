# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 10:36
from __future__ import unicode_literals

import consent.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consent', '0012_auto_20170214_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='educationdetail',
            name='college_passout_year',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='educationdetail',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to=consent.models.resume_file_path),
        ),
    ]
