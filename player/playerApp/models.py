from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from PIL import Image


class ImagesField(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=180)
    timeIn = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='images', null=True, blank=True, default='images/default/default.png')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save()
        photo_path = (self.photo.path)
        img = Image.open(photo_path)
        print('self.photo.path:', self.photo.path)
        print('img:', img)
        print(f'img.format: {img.format}, img.size: {img.size}, img.mode: {img.mode}')

        try:
            if img.height > 2000 or img.width > 4500:
                raise Exception
        except:
            print('Слишком большой размер')

        # if img.height > 2000 or img.width > 4500:
        #     raise Exception('Слишком большой размер')

        if img.height > 450 or img.width > 600:
            new_img = (600, 450)
            img.thumbnail(new_img)
            img.save(photo_path)

    def get_absolute_url(self):
        return reverse('files:imagesFieldPhoto', args=[str(self.id)])


class FilesField(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=180)
    timeIn = models.DateTimeField(auto_now_add=True)
    photo = models.FileField(upload_to='PDF', null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save()
        print("MODEL", self.photo.size)
        if self.photo.size > 1500000:
            raise Exception('Слишком большой размер PDF-файла')
