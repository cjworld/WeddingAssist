from rest_framework import generics, permissions, viewsets
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from parties.serializers import PhotoSerializer, PartySerializer, MessageSerializer, ParticipationWillingnessSerializer
from parties.models import Photo, Party, Message, ParticipationWillingness

'''
@login_required
def Index(request):
    context = {}
    return render(request, 'noters/index.html', context)
'''
class PhotoList(generics.ListCreateAPIView):
	model = Photo
	serializer_class = PhotoSerializer
	
	def get_queryset(self):
		queryset = super(PhotoList, self).get_queryset()
		return queryset.filter(author__username=self.request.user.username)
	
	def pre_save(self, obj):
		obj.author = self.request.user
		return super(PhotoList, self).pre_save(obj)
	
class PhotoDetail(generics.RetrieveUpdateDestroyAPIView):
	model = Photo
	serializer_class = PhotoSerializer
	permission_classes = [
		permissions.AllowAny
	]

class PartyList(generics.ListCreateAPIView):
	model = Party
	serializer_class = PartySerializer
	
	def get_queryset(self):
		queryset = super(PartyList, self).get_queryset()
		return queryset.filter(author__username=self.request.user.username)
	
	def pre_save(self, obj):
		obj.author = self.request.user
		return super(PartyList, self).pre_save(obj)
	
class PartyDetail(generics.RetrieveUpdateDestroyAPIView):
	model = Party
	serializer_class = PartySerializer
	permission_classes = [
		permissions.AllowAny
	]
	
class MessageList(generics.ListCreateAPIView):
	model = Message
	serializer_class = MessageSerializer
	
	def get_queryset(self):
		queryset = super(MessageList, self).get_queryset()
		return queryset.filter(author__username=self.request.user.username)
	
	def pre_save(self, obj):
		obj.author = self.request.user
		return super(MessageList, self).pre_save(obj)

class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
	model = Message
	serializer_class = MessageSerializer
	permission_classes = [
		permissions.AllowAny
	]
	
class ParticipationWillingnessList(generics.ListCreateAPIView):
	model = ParticipationWillingness
	serializer_class = ParticipationWillingnessSerializer
	
	def get_queryset(self):
		queryset = super(ParticipationWillingnessList, self).get_queryset()
		return queryset.filter(author__username=self.request.user.username)
	
	def pre_save(self, obj):
		obj.author = self.request.user
		return super(ParticipationWillingnessList, self).pre_save(obj)
	
class ParticipationWillingnessDetail(generics.RetrieveUpdateDestroyAPIView):
	model = ParticipationWillingness
	serializer_class = ParticipationWillingnessSerializer
	permission_classes = [
		permissions.AllowAny
	]
