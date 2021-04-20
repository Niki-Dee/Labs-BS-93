from .models import Beer
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class BeerForm(ModelForm):
    class Meta:
        model = Beer
        fields = ["title", "components", "about", "date"]

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название пива'
            }),
            "components": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Компоненты'
            }),
            "about": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Про пиво'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата'
            }),


        }