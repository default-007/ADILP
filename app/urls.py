from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', views.index, name='index'),
  path('about/', views.about, name='about'),
  path('services/', views.services, name='services'),
  path('events/', views.events, name='events'),
  path('events/<event>', views.posts, name='event'),
  path('services/<service>', views.service, name='service'),
  path('news/', views.news, name='news'),
  path('gallery/', views.gallery, name='gallery'),
  path('contact/', views.contact,name='contact'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)