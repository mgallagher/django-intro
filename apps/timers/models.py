from django.db import models


class Timer(models.Model):
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __unicode__(self):
        return self.description
