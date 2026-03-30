from django import forms
from .models import Genres, Track

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genres
        fields = ['name_ru', 'name_en', 'description']
        labels = {
            'name_ru': 'Название',
            'name_en': 'NAme',
            'description': 'Описание',
        }
