# Generated by Django 5.1.3 on 2024-11-13 20:26

import bagsApp.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bagsApp', '0020_rename_slugbag_bagsmodel_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='BagsPhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to=bagsApp.models.BagsPhotos.upload_location)),
                ('bags', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bagsApp.bagsmodel')),
            ],
        ),
    ]
