from django import forms
from pathlib import Path
from django.core.files.storage import default_storage

from django.core.exceptions import ValidationError

from .models import (ImagesField, FilesField)


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

    # error_messages = {
    #     NON_FIELD_ERRORS: {
    #         "error": "size",
    #     }
    # }


class PDFCreateForm(forms.ModelForm):
    title = forms.CharField(help_text="Введите название",
                            initial='PDF name')
    photo = forms.FileField()

    class Meta:
        model = FilesField
        fields = [
            'title',
            'photo'
        ]

    def clean(self):
        cleaned_data = super().clean()
        pdf = cleaned_data.get('photo')

        print(Path(str(pdf)))
        print(Path(str(pdf)).suffix)
        print(pdf.size)
        print(pdf.content_type)
        print(pdf.name)
        # print(default_storage.size(Path(str(pdf))))
        pdfSuffix = Path(str(pdf)).suffix
        if pdfSuffix != '.pdf':
            raise ValidationError(
                "Не PDF"
            )
        if pdf.size > 1000000:
            raise ValidationError(
                "Размер больше 1 МБ"
            )
        return cleaned_data
