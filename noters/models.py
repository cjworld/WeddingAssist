from django.db import models
from django.conf import settings
#from django.forms import ModelForm
#from schedules.models import Schedule
#from weddings.models import Wedding
#from places.models import Bakery, Venue

# ============= Blog ==============
'''
class Comment(models.Model):
	title = models.CharField(max_length=64)
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	datetime = models.DateTimeField()
	message = models.CharField(max_length=256)
    
class Blog(models.Model):
	title = models.CharField(max_length=64)
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	datetime = models.DateTimeField()
	abstract = models.CharField(max_length=256)
	content = models.CharField(max_length=10240)
	comments = models.ManyToManyField(Comment)
    
class Alarm(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    schedule = models.ForeignKey(Schedule)
    title = models.CharField(max_length=64)
    
    def __unicode__(self):
        return self.title
'''

class Notebook(models.Model):
    title = models.CharField(max_length=63)
    subscription = models.CharField(max_length=255, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    partners = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='notebooks')
    #watching_venues = models.ManyToManyField(Venue, blank=True)
    #watching_bakeries = models.ManyToManyField(Bakery, blank=True)
    
    def __unicode__(self):
        return self.title

class Memo(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    recipients = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='memos')
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=63, blank=True)
    message = models.CharField(max_length=255)
    alarm = models.BooleanField(blank=True)
    #blogs = models.ManyToManyField(Blog)
    datetime = models.DateTimeField(blank=True, null=True)
    notebook = models.ForeignKey(Notebook, blank=True, null=True, related_name='memos')
    
    def __unicode__(self):
        return self.message




'''
# ===========  Form ==========

class MemoForm(ModelForm):
    class Meta:
        model = Memo
#fields = ['name', 'title', 'birth_date']
'''