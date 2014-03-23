from django.db import models
from django.contrib.auth.models import User
	
class Photo(models.Model):
	author = models.ForeignKey(User, related_name='photos')
	title = models.CharField(max_length=127, blank=True)
	datetime = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(upload_to="photos")
	
	def __unicode__(self):
		return '%s, %s, %s, %s' % (self.author, self.title, self.datetime, self.image)
	
class Party(models.Model):
	author = models.ForeignKey(User, related_name='parties')
	datetime = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=127)
	subscription = models.TextField(blank=True)
	date = models.DateField()
	time = models.TimeField()
	place = models.CharField(max_length=511, blank=True)
	photos = models.ManyToManyField(Photo, through='PartyPhoto', blank=True, null=True)
	
	def __unicode__(self):
		return '%s, %s, %s, %s, %s, %s, %s, %s' % (self.author, self.datetime, self.title, self.subscription, self.date, self.time, self.place, self.photos)
	
class PartyPhoto(models.Model):
	photo = models.ForeignKey(Photo)
	party = models.ForeignKey(Party)
		
class Message(models.Model):
	author = models.ForeignKey(User, related_name='messages')
	datetime = models.DateTimeField(auto_now_add=True)
	body = models.CharField(max_length=2047)
	party = models.ForeignKey(Party, related_name='messages')
	
	def __unicode__(self):
		return '%s, %s, %s, %s' % (self.author, self.datetime, self.body, self.party)
		
class ParticipationWillingness(models.Model):
	author = models.ForeignKey(User, related_name='participationwillingnesses')
	participation = models.BooleanField()
	invitation = models.BooleanField()
	host = models.BooleanField()
	vegetarian = models.BooleanField()
	party = models.ForeignKey(Party, related_name='participationwillingnesses')
	
	def __unicode__(self):
		return '%s, %s, %s, %s, %s, %s' % (self.author, self.participation, self.invitation, self.host, self.vegetarian, self.party)
	