import datetime

from django.db import models
from django.utils import timezone


class NewsStory(models.Model):
    news_heading = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    news_story = models.CharField(max_length=500)

    def __str__(self):
        return self.news_heading

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.news_story

