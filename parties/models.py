from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
    
class Photo(models.Model):
    author = models.ForeignKey(User, related_name='photos')
    title = models.CharField(max_length=127, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images")
    
    def __unicode__(self):
        return '%s, %s, %s, %s' % (self.author, self.title, self.datetime, self.image)
    
class Party(models.Model):
    author = models.ForeignKey(User, related_name='parties')
    datetime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=127)
    subscription = models.TextField(blank=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    place = models.CharField(max_length=511, blank=True)
    photos = models.ManyToManyField(Photo, through='PartyPhoto', blank=True, null=True)
    
    def __unicode__(self):
        return '%s, %s, %s, %s, %s, %s, %s, %s' % (self.author, self.datetime, self.title, self.subscription, self.date, self.time, self.place, self.photos)

    def get_absolute_url(self):
        return reverse('parties:party-detail', args=[str(self.id)])
    
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

    def get_absolute_url(self):
        return reverse('parties:message-detail', args=[str(self.id)])
        
class Willingness(models.Model):
    author = models.ForeignKey(User, related_name='willingnesses')
    participation = models.BooleanField()
    invitation = models.BooleanField()
    host = models.BooleanField()
    vegetarian = models.BooleanField()
    party = models.ForeignKey(Party, related_name='willingnesses')
    
    def __unicode__(self):
        return '%s, %s, %s, %s, %s, %s' % (self.author, self.participation, self.invitation, self.host, self.vegetarian, self.party)

    def get_absolute_url(self):
        return reverse('parties:willingness-detail', args=[str(self.id)])
    