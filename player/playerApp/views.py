from django.shortcuts import render
from django.views.generic import ListView
from .models import (ImagesField)


class ImagesFieldView(ListView):
    model = ImagesField
    ordering = '-timeIn'
    template_name = 'viewsHTML/imagesField.html'
    context_object_name = 'imagesField'
