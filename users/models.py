from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    DEFAULT_IMAGE = 'default.jpg'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default=f'profile_pics/{DEFAULT_IMAGE}',
        upload_to='profile_pics')

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)


    def __str__(self):
        return f'{self.user.username} Profile'
