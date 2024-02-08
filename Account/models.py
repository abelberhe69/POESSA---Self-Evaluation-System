from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    REQUIRED_FIELDS=['first_name','last_name']
    DEP_CHOICES = [
        ('dep1', 'Dep1'),
        ('dep2', 'Dep2'),
        ('dep3', 'Dep3'),
    ]
    department = models.CharField(max_length=20, choices=DEP_CHOICES)
    ROLE_CHOICES = [
        ('director', 'Director'),
        ('team_leader', 'Team leader'),
        ('expert', 'Expert'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

