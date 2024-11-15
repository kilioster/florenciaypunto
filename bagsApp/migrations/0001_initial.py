# Generated by Django 5.1.3 on 2024-11-08 12:40

import multiselectfield.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BagsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('description', models.TextField()),
                ('material', multiselectfield.db.fields.MultiSelectField(choices=[('Algodon', 'Algodon'), ('Huaipe', 'Huaipe'), ('Poliester', 'Poliester'), ('Acetato', 'Acetato'), ('Lana', 'Lana')], max_length=50)),
                ('price', models.IntegerField(max_length=6)),
            ],
        ),
    ]
