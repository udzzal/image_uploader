from django import forms
from .models import Image_uploder

class Image_form(forms.ModelForm):
    class Meta:
        model=Image_uploder
        fields='__all__'
        labels={'image':''}
    
    