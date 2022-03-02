from django.shortcuts import redirect, render
from .forms import *
from django.template import loader

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
  context = {

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
      return redirect('index')
  else:
    form=SubscribersForm()
  context = {
    'form': form,
  }
  return render(request,'contact.html', context)