from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class NewUser(AbstractUser):
    surname = models.CharField(max_length=100)
    phone  = models.CharField(max_length=100)
    religion = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'NewUser: {self.firstname} {self.surname}' 