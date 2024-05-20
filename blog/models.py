from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied



User = get_user_model()
User= settings.AUTH_USER_MODEL



class salon(models.Model):
    author= models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="blog_images", null=True, blank=True)
    nom_salon = models.CharField(unique=False, max_length=100)
    pub_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    #type_salon = models.CharField(max_length=10, choices=salon_type.choices)
    is_published = models.BooleanField(default=False)
    boss = models.CharField(unique=False, max_length=100)
    contact = models.CharField(unique=False, max_length=100)
    def __str__(self):
     return self.nom_salon

    def get_absolute_url(self):
        return "/blog/post/" + str(self.id) + "/"
    
class TypeSalon(models.TextChoices):
    MIXTE = "Mixte"
    HOMME = "Homme"
    FEMME = "Femme"

class product(models.Model):
    author= models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    nom_produit=models.CharField(unique=False, max_length=100)
    photos=models.ImageField(upload_to="blog_images", null=True, blank=True)
    prix=models.IntegerField(default=0)
    origine=models.CharField(unique=False, max_length=100)
    quantite=models.IntegerField(default=1)
    description=models.CharField(unique=False, max_length=300)
    def __str__(self):
     return self.nom_produit

    def get_absolute_url(self):
        return "/blog/product/" + str(self.id) + "/"

class dailyPost(models.Model):
    photo=models.ImageField(upload_to="blog_images", null=True, blank=True)
    commentaire=models.CharField(unique=False, max_length=100)
    post_date=models.DateField(null=True, blank=True)
    def __str__(self):
     return self.commentaire





