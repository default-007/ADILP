from django import forms
from .models import *

class SubscribersForm(forms.ModelForm):
  class Meta:
    model = Subscriber
    fields = ["email","name"]

class MailMessageForm(forms.ModelForm):
  class Meta:
    model = MailMessage
    fields = '__all__'

class EventForm(forms.ModelForm):
  class Meta:
    model = Event
    fields = '__all__'