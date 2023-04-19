from django import forms
from .models import (ImagesField)


class ImagesFieldForm(forms.ModelForm):
    class Meta:
        model = ImagesField
        fields = [
            'user',
            'title',
            'photo'
        ]
