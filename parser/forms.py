from django import forms
from . import parser, models

class ParserForm(forms.Form):
    LAPTOP_CHOICES = (
        ('LAPTOPS_KG', 'LAPTOPS_KG'),
    )
    media_type = forms.ChoiceField(choices=LAPTOP_CHOICES)

    class Meta:
        field = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['media_type'] == 'LAPTOPS_KG':
            laptop_parser = parser.parser()
            for i in laptop_parser:
                models.Laptop.objects.create(**i)