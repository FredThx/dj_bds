'''A executer dans le shell Django
'''
import mysql.connector
from mesBDs.models import Auteur, Editeur, Serie, Livre
import datetime

old_bds = mysql.connector.connect(host = '192.168.10.174', user = 'fred', password = 'GaZoBu', database = 'BandeDessinee')
old_bds_cur = old_bds.cursor()


req = "SELECT * FROM Auteur"
old_bds_cur.execute(req)
for auteur in old_bds_cur.fetchall():
    new_auteur = Auteur(id = auteur[0], nom = auteur[1], prenom = auteur[2], commentaire = auteur[3])
    print(new_auteur)
    new_auteur.save()

req = "SELECT * FROM Editeur"
old_bds_cur.execute(req)
for editeur in old_bds_cur.fetchall():
    new_editeur = Editeur(id = editeur[0], nom = editeur[1], commentaire = editeur[2], site_web = editeur[3])
    print(new_editeur)
    new_editeur.save()

req = "SELECT * FROM Serie"
old_bds_cur.execute(req)
for serie in old_bds_cur.fetchall():
    new_serie = Serie(id = serie[0], nom = serie[1], terminee = serie[2]==-1, prevision = serie[3])
    print(new_serie)
    new_serie.save()

req = "SELECT * FROM Livre"
old_bds_cur.execute(req)
for livre in old_bds_cur.fetchall():
    if not Livre.objects.filter(id = livre[0]):
        new_livre = Livre.objects.create(id = livre[0],
                        titre = livre[1],
                        tome = livre[2],
                        serie = Serie.objects.filter(id=livre[3])[0],
                        auteur1 = Auteur.objects.filter(id=livre[4])[0],
                        auteur2 = livre[5] and Auteur.objects.filter(id=livre[5])[0],
                        editeur = Editeur.objects.filter(id=livre[6])[0],
                        annee_premiere_edition = livre[7],
                        annee_edition = livre[8],
                        date_achat = livre[9],
                        prix = livre[10],
                        commentaire = livre[11],
                        couverture = "ImagesBD/"+livre[12])
        print(new_livre)
        new_livre.save()
        print("saved.")


for livre in Livre.objects.all():
    if str(livre.couverture).split('/')[1] == "images":
        livre.couverture = '/'.join(str(livre.couverture).split('/')[2:])
        livre.save()
        print(livre)
