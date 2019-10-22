from django.contrib.auth.models import AbstractUser
from django.db import models


class MainUser(AbstractUser):
    is_guest = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False) # store admin

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name


class Profile(models.Model):
    phone = models.CharField(max_length=11)
    address = models.TextField(max_length=100)
    user = models.OneToOneField(MainUser, on_delete=models.CASCADE)