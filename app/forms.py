from django import forms
from .models import *

class SubscribersForm(forms.ModelForm):
  class Meta:
    model = Subscriber
    fields = ["email","name"]

class EventForm(forms.ModelForm):
  def __init__(self, *args,**kwargs):
    super().__init__(*args, **kwargs)
    self.fields['pictures']= forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}))

  class Meta:
    model = Event
    fields = '__all__'