from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from PIL import Image
from ckeditor.fields import RichTextField


# Create your models here.
class Utilisateur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=0)
    Address = models.CharField(max_length=255, null=True)
    City = models.CharField(max_length=255, null=True)
    Country = models.CharField(max_length=255, null=True)
    postal_code = models.CharField(max_length=20, null=True)
    about_me = models.TextField(null=True)
    avatar = models.ImageField(default='Tortuga.png', upload_to='profile_images')
    phonenumber = models.CharField(max_length=20, null=True)
    date_naissance = models.DateField(null=True)
    
    USERNAME_FIELD = 'pseudo'



    
   
    
         
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Utilisateur.objects.create(user=instance)


    

class Admin(models.Model):
    id_admin =models.OneToOneField(Utilisateur,on_delete=models.CASCADE, primary_key = True)

class infopreneur(models.Model):
    id_infopreneur =models.OneToOneField(Utilisateur,on_delete=models.CASCADE, primary_key = True)

class Contactt(models.Model):
    id_c= models.IntegerField(primary_key = True)
    id_infopreneur =models.ForeignKey(infopreneur,on_delete=models.CASCADE)

class Contact(models.Model):
    name = models.CharField(max_length=100)  
    email = models.EmailField(null=True)  
    contact = models.CharField(max_length=15)
   
    class Meta:  
        db_table = "Contactt"

   
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
    reference=models.IntegerField(primary_key = True)
    id_infopreneur =models.ForeignKey(infopreneur,on_delete=models.CASCADE)
    id_produit =models.ForeignKey(Produit,on_delete=models.CASCADE)
    id_contact =models.ForeignKey(Contact,on_delete=models.CASCADE)
    date_vente=models.DateField()
    quantite= models.IntegerField()

class Affilie(models.Model):
     
     id_infopreneur =models.ForeignKey(infopreneur,on_delete=models.CASCADE,default='0')
     id_produit =models.ForeignKey(Produit,on_delete=models.CASCADE,default='0')
     nom_prenom=models.CharField(max_length=60,null=True)
     email = models.EmailField(null=True)  
     contact = models.CharField(max_length=15,null=True)
     contrat=RichTextField(null=True)
     pourcentage=models.CharField(max_length=15,null=True)


class TemplatesCommuns(models.Model):
     id = models.AutoField(primary_key=True)
     title = models.CharField(max_length=30,null=True)
     codeHtml=models.TextField(null=True)
     type=models.CharField(max_length=30,null=True)
     image = models.ImageField(null=True)
     
class TemplatesUser(models.Model):
     id= models.IntegerField(primary_key = True)
     title = models.CharField(max_length=30,null=True)
     codeHtml=models.TextField(null=True)
     type=models.CharField(max_length=30,null=True)
     URL=models.TextField(null=True)
     description=models.TextField(null=True)
     id_infopreneur =models.ForeignKey(infopreneur,on_delete=models.CASCADE,default='0')
     id_Commun =models.ForeignKey(TemplatesCommuns,on_delete=models.CASCADE,default='0')
     image = models.ImageField(null=True)

class ContactFormSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=20,null=True)
    subject = models.CharField(max_length=200,null=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

class ContactGoogle(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"