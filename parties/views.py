from rest_framework import generics, permissions, viewsets
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from parties.serializers import PhotoSerializer, PartySerializer, MessageSerializer, ParticipationWillingnessSerializer
from parties.models import Photo, Party, Message, ParticipationWillingness
'''
class PhotoList(generics.ListAPIView):
	model = Photo
	serializer_class = PhotoSerializer
	
	def get_queryset(self):
		queryset = super(PhotoList, self).get_queryset()
        return queryset
        #return queryset.filter(author__username=self.request.user.username)
	
class PhotoDetail(generics.RetrieveAPIView):
	model = Photo
	serializer_class = PhotoSerializer
	permission_classes = [
		permissions.AllowAny
	]
'''
class PartyList(generics.ListAPIView):
	model = Party
	serializer_class = PartySerializer
	
	def get_queryset(self):
		queryset = super(PartyList, self).get_queryset()
        return queryset
	
class PartyDetail(generics.RetrieveAPIView):
	model = Party
	serializer_class = PartySerializer
	permission_classes = [
		permissions.AllowAny
	]

class PartyMessageList(generics.ListAPIView):
    model = Message
    serializer_class = MessageSerializer
    
    def get_queryset(self):
        queryset = super(PartyMessageList, self).get_queryset()
        return queryset.filter(party__pk=self.kwargs.get('pk'))
'''
class PartyParticipationWillingnessDetail(generics.RetrieveUpdateDestroyAPIView):
    model = ParticipationWillingness
    serializer_class = ParticipationWillingnessSerializer
    
    def get_queryset(self):
        queryset = super(PartyParticipationWillingnessDetail, self).get_queryset()
        return queryset.filter(party__pk=self.kwargs.get('pk'), author__username==self.request.user.username)

class ParticipationWillingnessList(generics.ListAPIView):
	model = ParticipationWillingness
	serializer_class = ParticipationWillingnessSerializer
	
	def get_queryset(self):
		queryset = super(ParticipationWillingnessList, self).get_queryset()
        return queryset
		#return queryset.filter(author__username=self.request.user.username)
	
	def pre_save(self, obj):
		obj.author = self.request.user
		return super(ParticipationWillingnessList, self).pre_save(obj)

class ParticipationWillingnessDetail(generics.RetrieveAPIView):
	model = ParticipationWillingness
	serializer_class = ParticipationWillingnessSerializer
	permission_classes = [
		permissions.AllowAny
	]
'''
class UserPartyList(generics.ListCreateAPIView):
    model = Party
    serializer_class = PartySerializer
    
    def get_queryset(self):
        queryset = super(UserPartyList, self).get_queryset()
        return queryset.filter(author__username=self.request.user.username)
    
    def pre_save(self, obj):
        obj.author = self.request.user
        return super(UserPartyList, self).pre_save(obj)

class UserPartyDetail(generics.RetrieveUpdateDestroyAPIView):
	model = Party
	serializer_class = PartySerializer
	permission_classes = [
        permissions.AllowAny
    ]

class UserParticipationWillingnessList(generics.ListAPIView):
    model = ParticipationWillingness
    serializer_class = ParticipationWillingnessSerializer
    
    def get_queryset(self):
        queryset = super(UserParticipationList, self).get_queryset()
        return queryset.filter(author__username=self.request.user.username)

class UserParticipationWillingnessCreate(generics.CreateAPIView):
    model = ParticipationWillingness
    serializer_class = ParticipationWillingnessSerializer
    
    def pre_save(self, obj):
        obj.author = self.request.user
        return super(UserParticipationWillingnessCreate, self).pre_save(obj)

class UserParticipationWillingnessDetail(generics.RetrieveUpdateDestroyAPIView):
	model = ParticipationWillingness
	serializer_class = ParticipationWillingnessSerializer
	permission_classes = [
        permissions.AllowAny
    ]

class UserMessageList(generics.ListAPIView):
	model = Message
	serializer_class = MessageSerializer
	
	def get_queryset(self):
		queryset = super(MessageList, self).get_queryset()
		return queryset.filter(author__username=self.request.user.username)

class UserMessageCreate(generics.CreateAPIView):
	model = Message
	serializer_class = MessageSerializer
	
    def pre_save(self, obj):
		obj.author = self.request.user
		return super(UserMessageCreate, self).pre_save(obj)

class UserMessageDetail(generics.RetrieveUpdateDestroyAPIView):
	model = Message
	serializer_class = MessageSerializer
	permission_classes = [
        permissions.AllowAny
    ]
'''
class UserPhotoList(generics.ListCreateAPIView):
    model = Photo
    serializer_class = PhotoSerializer
    
    def get_queryset(self):
        queryset = super(UserPhotoList, self).get_queryset()
        return queryset.filter(author__username=self.request.user.username)

    def pre_save(self, obj):
        obj.author = self.request.user
        return super(UserPhotoList, self).pre_save(obj)

class UserPhotoDetail(generics.RetrieveUpdateDestroyAPIView):
	model = Photo
	serializer_class = PhotoSerializer
	permission_classes = [
        permissions.AllowAny
    ]

'''