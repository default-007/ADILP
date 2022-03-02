from django.shortcuts import redirect, render
from .forms import *
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string

# Create your views here.

def index(request):
  
  context = {

  }
  return render(request, 'index.html', context)

def about(request):
  
  context = {

  }
  return render(request, 'about.html', context)

def mail_letters(request):
  if request.method == 'POST':
    form=MailMessageForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'Message has ben sent to mail list')
  else:
    form=MailMessageForm()
  context = {
    'form': form,
  }
  return render(request, '', context)

def services(request):
  context = {

  }
  return render(request, 'services.html', context)

def news(request):
  context = {}
  return render(request,'press.html', context)

def posts(request):
  context = {}
  return render(request,'post.html', context)

def contact(request):
  if request.method == 'POST':
    
    form=SubscribersForm(request.POST)
    if form.is_valid():
      form.save()
      name = form.cleaned_data.get('name')
      to_email = form.cleaned_data.get('email')
      current_site = get_current_site(request)
      mail_subject = 'Thank you for registering to our site'
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