from django.db import models
from django.contrib.auth.models import User


class ImagesField(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=180)
    timeIn = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='images', null=True, blank=True, default='images/default/default.png')

    def __str__(self):
        return self.title
