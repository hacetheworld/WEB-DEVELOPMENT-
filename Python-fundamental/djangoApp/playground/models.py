from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
# class ToDoList(models.Model):


class Contact(models.Model):
    email = models.CharField(max_length=122)
    message = models.CharField(max_length=122)
    date = models.DateField()

    def __str__(self) -> str:
        return self.email
