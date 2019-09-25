from django.db import models
from django.contrib.auth.models import AbstractUser
from project import settings


class MainUser(AbstractUser):
    is_creator = models.BooleanField(default=True)
    is_executor = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return str(self.id) + ' ' + self.username


class Profile(models.Model):
    bio = models.TextField(max_length=500)
    address = models.TextField(max_length=300)
    web_site = models.CharField(max_length=30)
    avatar = models.ImageField()
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    joined_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username

