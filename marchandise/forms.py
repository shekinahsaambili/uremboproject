from django import forms
from .models import marchandisePost

class marchandisePostForm(forms.ModelForm):
    class Meta:
        model = marchandisePost
        fields = [ 'title', 'content', 'is_published' , 'price', ]