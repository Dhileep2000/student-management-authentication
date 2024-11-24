from django.db import models
from django.contrib.auth.models import AbstractUser

class student_model(AbstractUser):

    age=models.PositiveIntegerField(default=0)
    