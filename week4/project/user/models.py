from django.db import models
from django.contrib.auth.models import AbstractUser
from project import settings


class MainUser(AbstractUser):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return str(self.id) + ' ' + self.username


class Profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField(max_length=500, blank=True, default='')
    address = models.TextField(max_length=300)
    web_site = models.CharField(max_length=30, blank=True, default='')
    avatar = models.ImageField(null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    joined_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'profile'
        ordering = ('joined_at', )

    def __str__(self):
        return self.user.username

    @property
    def full_name(self):
        return self.first_name + '' + self.last_name


