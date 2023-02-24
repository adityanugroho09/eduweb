from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def save(self, *awrgs, **kwargs):
        super().save()
        img = Image.open(self.avatar.path)
        img.save(self.avatar.path)
        
    def __str__(self):
        return f"{self.user.username} Profile"

