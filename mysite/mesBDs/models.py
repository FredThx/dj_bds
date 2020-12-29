from django.db import models

import datetime
from django.utils import timezone
from django.utils.html import mark_safe
from django.core.validators import MaxValueValidator, MinValueValidator
import computed_property


class Auteur(models.Model):
    '''Un auteur de BDs
    '''
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    commentaire = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Editeur(models.Model):
    '''Un éditeur de BDs
    '''
    nom = models.CharField(max_length=30)
    commentaire = models.CharField(max_length=300)
    site_web = models.URLField(max_length=100)

    def __str__(self):
        return self.nom

class Serie(models.Model):
    '''Une série de BDs
    '''
    articles = ['Le ','le ','La ','la ','Un ','un ','Une ','une ',"L'","l'","Les ","les "]
    nom = models.CharField(max_length=30)
    terminee = models.BooleanField()
    prevision = models.CharField(max_length=30)
    nom2 = computed_property.ComputedCharField(compute_from='_nom2', max_length=30, default = "")

    def __str__(self):
        return self.nom

    def _nom2(self):
        for article in sorted(self.articles, key= len):
            if self.nom[:len(article)]==article:
                return self.nom[len(article):]
        return self.nom

class Livre(models.Model):
    '''Une BD
    '''
    titre = models.CharField(max_length=50)
    tome = models.IntegerField()
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    auteur1 = models.ForeignKey(Auteur, on_delete=models.CASCADE, related_name = '%(class)s_auteur1')
    auteur2 = models.ForeignKey(Auteur, on_delete=models.CASCADE, related_name = '%(class)s_auteur2', blank=True, null = True)
    editeur = models.ForeignKey(Editeur, on_delete=models.CASCADE)
    annee_premiere_edition = models.IntegerField(validators = [MinValueValidator(1900), MaxValueValidator(3000)])
    annee_edition = models.IntegerField(validators = [MinValueValidator(1900), MaxValueValidator(3000)])
    date_achat = models.DateField("date d'achat", null = True, blank = True)
    prix = models.DecimalField(max_digits = 5, decimal_places = 2)
    commentaire = models.CharField(max_length=300, blank=True)
    couverture = models.ImageField() #need Piloww !!!

    def __str__(self):
        return self.titre

    def image_tag(self):
        return mark_safe('<img src="/directory/%s" width="150" height="150" />' % (self.couverture))
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
