from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Task(models.Model):
    title = models.CharField(max_length=64)
    note = models.CharField(max_length=256)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    # Define constants for priority
    HIGH = 1
    MID = 2
    LOW = 3
    priorities = (
        (HIGH, "!!!"),
        (MID, "!!"),
        (LOW, "!")
    )
    # Pass in None for this field in order to save it as NULL.
    priority = models.IntegerField(choices=priorities, null=True, blank=True)