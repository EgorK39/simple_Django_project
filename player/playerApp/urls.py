from django.urls import path
from .views import (
    ImagesFieldView, ImagesFieldViewCreate, ImagesFieldViewDetail)

urlpatterns = [
    path('images/', ImagesFieldView.as_view(), name='imagesField'),
    path('images/<int:pk>', ImagesFieldViewDetail.as_view(), name='imagesFieldPhoto'),
    path('create/', ImagesFieldViewCreate.as_view(), name='imagesFieldViewCreate'),

]
