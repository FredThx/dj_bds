# Generated by Django 3.1.4 on 2020-12-27 15:33

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auteur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('commentaire', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Editeur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('commentaire', models.CharField(max_length=300)),
                ('site_web', models.URLField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('terminee', models.BooleanField()),
                ('prevision', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('tome', models.IntegerField()),
                ('annee_premiere_edition', models.IntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(3000)])),
                ('annee_edition', models.IntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(3000)])),
                ('date_achat', models.DateTimeField(verbose_name="date d'achat")),
                ('prix', models.DecimalField(decimal_places=2, max_digits=5)),
                ('commentaire', models.CharField(max_length=300)),
                ('couverture', models.ImageField(upload_to='')),
                ('auteur1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='livre_auteur1', to='mesBDs.auteur')),
                ('auteur2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='livre_auteur2', to='mesBDs.auteur')),
                ('editeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mesBDs.editeur')),
                ('serie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mesBDs.serie')),
            ],
        ),
    ]