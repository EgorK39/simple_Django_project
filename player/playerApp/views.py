import os.path

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, DetailView)
from .models import (ImagesField)
from .forms import (ImagesFieldForm)


class ImagesFieldView(ListView):
    model = ImagesField
    ordering = '-timeIn'
    template_name = 'viewsHTML/imagesField.html'
    context_object_name = 'imagesField'


class ImagesFieldViewCreate(LoginRequiredMixin, CreateView):
    form_class = ImagesFieldForm
    model = ImagesField
    template_name = 'viewsHTML/imagesFieldCreate.html'
    success_url = reverse_lazy('files:imagesField')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ImagesFieldViewDetail(DetailView):
    model = ImagesField
    template_name = 'viewsHTML/imagesFieldDetail.html'
    context_object_name = 'imagesFieldDetail'
