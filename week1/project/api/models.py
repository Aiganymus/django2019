from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=120)
    created_at = models.DateField(auto_now_add=True)
    address = models.TextField(max_length=200)
    boss = models.ForeignKey(User, on_delete=models.CASCADE)
