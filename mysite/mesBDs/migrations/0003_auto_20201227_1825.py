# Generated by Django 3.1.4 on 2020-12-27 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mesBDs', '0002_auto_20201227_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livre',
            name='date_achat',
            field=models.DateField(blank=True, null=True, verbose_name="date d'achat"),
        ),
    ]
