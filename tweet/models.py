from django.db import models

from django.utils import timezone

from twitteruser.models import TwitterUser

# Create your models here.


class Tweets(models.Model):
    author = models.ForeignKey(TwitterUser, on_delete=models.CASCADE, related_name='author', null=True)
    message = models.CharField(max_length=140)
    publish_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.message} - {self.publish_date}"
