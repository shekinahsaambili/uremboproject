from django import forms
from .models import salon, product



class salonform(forms.ModelForm):
    class Meta:
        model = salon
        fields = ['nom_salon', 'description', 'image', 'is_published' , 'pub_date', 'boss', 'contact']

class productform(forms.ModelForm):
    class Meta:
        model = product
        fields =['nom_produit', 'photos', 'prix', 'origine', 'author', 'quantite', 'description']
        