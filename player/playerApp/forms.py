from django import forms
from .models import (ImagesField)


class ImagesFieldForm(forms.ModelForm):
    title = forms.CharField(help_text="Введите название",
                            initial='title')
    photo = forms.ImageField()

    class Meta:
        model = ImagesField
        fields = [
            'title',
            'photo'
        ]


