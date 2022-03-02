from django.db import models

# Create your models here.

class Subscriber(models.Model):
  name = models.CharField(max_length=255, null=True)
  email = models.EmailField(null=True)
  date_joined = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.email

  
class MailMessage(models.Model):
  title = models.CharField(max_length =100, null=True)
  message = models.TextField(null=True)

  def __str__(self):
    return self.title

class News_video(models.Model):
  video_link = models.URLField(max_length=300, null=True)
  date = models.DateField(null=True, blank=True)

class Event(models.Model):
  headline = models.CharField(max_length=100, null=True)
  description = models.TextField()
  date = models.DateField()

class Picture(models.Model):
  event = models.ForeignKey(Event, on_delete=models.CASCADE)
  file = models.ImageField()