from django.db import models

# Create your models here.
class Utilisateur(models.Model):
         id= models.IntegerField(primary_key = True)
         nom = models.CharField(max_length=25) 
         prenom = models.CharField(max_length=25) 
         pseudo = models.CharField(max_length=200) 
         email = models.EmailField(max_length=200)
         num_tel= models.IntegerField()
         date_naissance = models.DateField()  
         image = models.ImageField()
         USERNAME_FIELD = 'pseudo'
class Admin(models.Model):
    id_admin =models.OneToOneField(Utilisateur,on_delete=models.CASCADE, primary_key = True)

class infopreneur(models.Model):
    id_infopreneur =models.OneToOneField(Utilisateur,on_delete=models.CASCADE, primary_key = True)

class Contact(models.Model):
    id= models.IntegerField(primary_key = True)
    id_infopreneur =models.ForeignKey(infopreneur,on_delete=models.CASCADE)
    nom = models.CharField(max_length=25) 
    prenom = models.CharField(max_length=25) 
    email = models.CharField(max_length=200)
    num_tel= models.IntegerField()


class Produit(models.Model):
    id= models.IntegerField(primary_key = True)
    id_infopreneur =models.ForeignKey(infopreneur,on_delete=models.CASCADE)
    nom = models.CharField(max_length=25)    
    prix = models.DecimalField(max_digits=6, decimal_places=2)             
    description = models.CharField(max_length=500) 
    CATEGORIE = [
    ('img', 'IMAGE'),
    ('VD', 'VIDEO'),
    ('B', 'Ebook'),
    ('T', 'TICKET'),
    ('pdf', 'Portable Document Format'),
                ]


class Vente(models.Model):
    reference:models.IntegerField(primary_key = True)
    id_infopreneur =models.ForeignKey(infopreneur,on_delete=models.CASCADE)
    id_produit =models.ForeignKey(Produit,on_delete=models.CASCADE)
    id_contact =models.ForeignKey(Contact,on_delete=models.CASCADE)
    date_vente:models.DateField()
    quantite: models.IntegerField()

class Affiliation(models.Model):
     id_affilie:models.IntegerField()
     nom_affilie:models.CharField(max_length=30)
     prenom_affilie:models.CharField(max_length=30)

class Contrat(models.Model):
    id_contrat:models.IntegerField()
    id_infopreneur =models.ForeignKey(infopreneur,on_delete=models.CASCADE)
    id_produit =models.ForeignKey(Produit,on_delete=models.CASCADE)
    id_affilie= models.ForeignKey(Affiliation,on_delete=models.CASCADE)