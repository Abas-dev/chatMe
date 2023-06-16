from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    roomName = models.CharField(max_length=150,unique=True,null=False,blank=False)

    def __str__(self):
        return self.roomName