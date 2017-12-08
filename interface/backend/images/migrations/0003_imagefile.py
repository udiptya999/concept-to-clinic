# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-05 20:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_imageseries_patient_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slice_location', models.FloatField(null=True)),
                ('slice_thickness', models.FloatField(null=True)),
                ('rescale_slope', models.IntegerField(null=True)),
                ('rows', models.IntegerField(null=True)),
                ('columns', models.IntegerField(null=True)),
                ('pixel_spacing_col', models.FloatField(null=True)),
                ('pixel_spacing_row', models.FloatField(null=True)),
                ('path', models.FilePathField(path='/images', recursive=True)),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='images.ImageSeries')),
            ],
        ),
    ]