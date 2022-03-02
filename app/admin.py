from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *
from .forms import *

admin.site.register(MailMessage)
admin.site.register(News_video)
admin.site.register(Event)
admin.site.register(Picture)
# Register your models here.

class SubscriberResource(resources.ModelResource):
    class Meta:
        model = Subscriber
        fields = ('id', 'name', 'email',)
class SubscriberAdmin(ImportExportModelAdmin):
  resource_class = SubscriberResource

admin.site.register(Subscriber, SubscriberAdmin)
''' @admin.register(Event)
class EventAdmin(admin.ModelAdmin):
  list_display = ('headline',)
  add_form_template = 'admin/event_form.html'
  change_form_template = 'admin/event_form.html'

  def get_form(self, request, obj=None, *args, **kwargs):
    try:
      instance = kwargs['instance']
      return EventForm(instance=instance)
    except KeyError:
      return EventForm

  def add_view(self, request, form_url="", extra_context=None):
        extra_context = extra_context or {}
        extra_context['form'] = self.get_form(request)
        return super(EventAdmin, self).add_view(request, form_url=form_url, extra_context=extra_context)
    
  def change_view(self, request, object_id, form_url="", extra_context=None):
      extra_context = extra_context or {}
      post = Event.objects.get(id=object_id)
      extra_context["form"] = self.get_form(instance=post)
      return super(EventAdmin, self).change_view(request, object_id, form_url=form_url, extra_context=extra_context)

  def save_model(self, request, obj, form, change):
      obj.save()
      pictures = request.FILES.getlist('pictures')
      for picture in pictures:
          Picture.objects.create(post=obj, image=picture)
      return super().save_model(request, obj, form, change) '''