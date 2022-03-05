from django.db import models
from tinymce import models as tinymce_models
from django.utils.html import mark_safe
from markdown import markdown

# Create your models here.

class Subscriber(models.Model):
  name = models.CharField(max_length=255, null=True)
  email = models.EmailField(null=True)
  date_joined = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.email

  
class MailMessage(models.Model):
  title = models.CharField(max_length =100, null=True)
  message = tinymce_models.HTMLField(null=True)

  def __str__(self):
    return self.title

class News_video(models.Model):
  video_link = models.URLField(max_length=300, null=True)
  date = models.DateField(null=True, blank=True)

class Event(models.Model):
  headline = models.CharField(max_length=100, null=True)
  description = tinymce_models.HTMLField()
  date = models.DateField()

  def __str__(self):
    return self.headline

class Picture(models.Model):
  event = models.ForeignKey(Event, on_delete=models.CASCADE)
  file = models.ImageField()

class Gallery(models.Model):
  image = models.ImageField()

class Service(models.Model):
  title = models.CharField(max_length=100, null=True)
  image = models.ImageField(null=True, blank=True)
  description = tinymce_models.HTMLField()

  def __str__(self):
    return self.title
