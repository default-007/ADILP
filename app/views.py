from django.shortcuts import redirect, render
from .forms import *
from django.contrib import messages
from django.core.mail import EmailMessage
from django.utils.translation import gettext_lazy as _
from django.utils.translation import get_language, activate, gettext
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string

# Create your views here.

def index(request):
  news = News_video.objects.all()
  context = {
    'news': news,
  }
  return render(request, 'index.html', context)

def about(request):
  
  context = {

  }
  return render(request, 'about.html', context)

def gallery(request):
  images = Gallery.objects.all()
  context = {
    'images': images,
  }
  return render(request, 'gallery.html', context)

def services(request):
  services = Service.objects.all()
  context = {
    'services': services
  }
  return render(request, 'services.html', context)

def service(request, service):
  service = Service.objects.get(title=service)
  context = {
    'service': service,
  }
  return render(request, 'service.html', context)

def events(request):
  events = Event.objects.all()
  context={
    'events': events,
  }
  return render(request, 'events.html', context)

def news(request):
  news = News_video.objects.all()
  context = {
    'news': news,
  }
  return render(request,'press.html', context)

def posts(request, event):
  event = Event.objects.get(headline=event)
  context = {
    'event': event,
  }
  return render(request,'post.html', context)

def contact(request):
  if request.method == 'POST':
    
    form=SubscribersForm(request.POST)
    if form.is_valid():
      form.save()
      name = form.cleaned_data.get('name')
      to_email = form.cleaned_data.get('email')
      current_site = get_current_site(request)
      mail_subject = _('Thank you for registering to our site')
      message = render_to_string('acc_active_email.html', {
                  'name': name,
                  'domain': current_site.domain,
              })
      email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
      email.send()
      messages.success(request, 'Subscription successful')
  else:
    form=SubscribersForm()
  context = {
    'form': form,
  }
  return render(request,'contact.html', context)

def translate(language):
  cur_language = get_language()
  try:
    activate(language)
    text=gettext('hello')
  finally:
    activate(cur_language)
  return text