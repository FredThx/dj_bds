# Generated by Django 3.1.4 on 2020-12-27 22:17

import computed_property.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mesBDs', '0007_auto_20201227_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='serie',
            name='nom2',
            field=computed_property.fields.ComputedCharField(compute_from='_nom2', default='', editable=False, max_length=30),
        ),
    ]
