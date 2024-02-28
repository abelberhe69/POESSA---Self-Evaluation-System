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
    TEAM_CHOICES = [
        ('team1', 'Team1'),
        ('team2', 'Team2'),
        ('team3', 'Team3'),
    ]
    team = models.CharField(max_length=20, choices=TEAM_CHOICES, null=True)
    ROLE_CHOICES = [
        ('director', 'Director'),
        ('team_leader', 'Team leader'),
        ('expert', 'Expert'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    Leader = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

