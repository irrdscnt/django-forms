from django import forms
from .models import *

class AddForm(forms.ModelForm):

    class Meta:
        model = Serie
        fields = ('title','image','description','date')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),       
            'image': forms.FileInput(attrs={'class':'form-control'}),           
            'description': forms.TextInput(attrs={'class': 'form-control'}),           
            'date': forms.TextInput(attrs={'class': 'form-control'}),        
        }

class ImageForm(forms.ModelForm):
    class Meta:
        model:Serie
        fields=['image']