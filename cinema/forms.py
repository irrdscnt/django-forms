from django import forms
from .models import *
from . import parser, models

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

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('FILMS_KG', 'FILMS_KG'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        field = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['media_type'] == 'FILMS_KG':
            film_parser = parser.parser()
            for i in film_parser:
                models.TvParser.objects.create(**i)