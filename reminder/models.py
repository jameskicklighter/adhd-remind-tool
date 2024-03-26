from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Task(models.Model):
    title = models.CharField(max_length=64)
    note = models.CharField(max_length=256, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    class Priorities(models.IntegerChoices):
        HIGH = 1, "!!!"
        NORMAL = 2, "!!"
        LOW = 3, "!"
    # Pass in None for this field in order to save it as NULL.
    priority = models.IntegerField(choices=Priorities, null=True, blank=True)

    # category might be needed too to group to-dos.