from django.db import models

# Create your models here.

class Notification(models.Model):
    message = models.TextField()
    deadline = models.DateTimeField(auto_now=False, auto_now_add=False)

class NextEvents(models.Model):
    event_name = models.CharField(max_length=100,default="")
    event_bio = models.TextField()
    event_ends_on = models.DateTimeField(auto_now=False, auto_now_add=False)
    event_img = models.ImageField(upload_to='imgs/events')

    def __str__(self):
        return self.event_name
    