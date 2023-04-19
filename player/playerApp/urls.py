from django.urls import path
from .views import (ImagesFieldView)

urlpatterns = [
    path('images/', ImagesFieldView.as_view(), name='imagesField'),
]
