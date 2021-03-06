from django.contrib.auth.models import AbstractUser

from django.db import models

# Create your models here.


class TwitterUser(AbstractUser):
    name = models.CharField(max_length=150, null=True)
    follow = models.ManyToManyField("self", related_name='follow')

    def total_follows(self):
        return self.follow.count()

    def __str__(self):
        return f"{self.name}"
