from django.contrib import admin

# Register your models here.

from .models import Auteur, Editeur, Serie, Livre, Auteur

class LivreInLine(admin.TabularInline):
    model = Livre
    fieldsets = [
        (None, {'fields' : ['serie', 'titre', 'tome']}),
        ('Auteurs', {'fields' : ['auteur1', 'auteur2']}),
        ('Edition', {'fields' : ['editeur', 'annee_premiere_edition', 'annee_edition']}),
        ('Achat', {'fields' : ['date_achat', 'prix']}),
        (None, {'fields' : ['commentaire', 'image_tag']}),
    ]
    readonly_fields = ('image_tag',)
    extra = 0

class SerieAdmin(admin.ModelAdmin):
    inlines = [LivreInLine]
    search_fields = ['nom']
    ordering = ['nom']

admin.site.register(Serie, SerieAdmin)














admin.site.register(Auteur)

admin.site.register(Editeur)
