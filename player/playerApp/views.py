import os.path

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, DetailView)
from .models import (ImagesField, FilesField)
from .forms import (ImagesFieldForm, PDFCreateForm)


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


class PDFView(ListView):
    model = FilesField
    ordering = '-timeIn'
    template_name = 'viewsHTML/filesField.html'
    context_object_name = 'pdfField'


class PDFCreateView(LoginRequiredMixin, CreateView):
    form_class = PDFCreateForm
    model = FilesField
    template_name = 'viewsHTML/pdfCreateField.html'
    success_url = reverse_lazy('files:pdfView')

    def form_valid(self, form):
        form.instance.user = self.request.user
        print('self', self)
        return super().form_valid(form)
