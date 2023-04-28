# Generated by Django 4.2 on 2023-04-27 18:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('playerApp', '0002_alter_imagesfield_photo_alter_imagesfield_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilesField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=180)),
                ('timeIn', models.DateTimeField(auto_now_add=True)),
                ('photo', models.FileField(blank=True, null=True, upload_to='PDF')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]