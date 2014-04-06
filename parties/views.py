from rest_framework import generics, permissions, viewsets
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from parties.serializers import PhotoSerializer, PartySerializer, MessageSerializer, WillingnessSerializer
from parties.models import Photo, Party, Message, Willingness

class PhotoList(generics.ListCreateAPIView):
    model = Photo
    serializer_class = PhotoSerializer
    permission_classes = [
        permissions.AllowAny
    ]
    
    def pre_save(self, obj):
        obj.author = self.request.user
        return super(PhotoList, self).pre_save(obj)
    
class PhotoDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Photo
    serializer_class = PhotoSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class UserPhotoList(generics.ListAPIView):
    model = Photo
    serializer_class = PhotoSerializer
    permission_classes = [
        permissions.AllowAny
    ]
    
    def get_queryset(self):
        queryset = super(UserPhotoList, self).get_queryset()
        return queryset.filter(author__username=self.request.user.username)

class PartyList(generics.ListCreateAPIView):
    model = Party
    serializer_class = PartySerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def pre_save(self, obj):
        obj.author = self.request.user
        return super(PartyList, self).pre_save(obj)
    
class PartyDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Party
    serializer_class = PartySerializer
    permission_classes = [
        permissions.AllowAny
    ]

class PartyMessageList(generics.ListAPIView):
    model = Message
    serializer_class = MessageSerializer
    permission_classes = [
        permissions.AllowAny
    ]
    
    def get_queryset(self):
        queryset = super(PartyMessageList, self).get_queryset()
        return queryset.filter(party__pk=self.kwargs.get('pk'))

class PartyWillingnessList(generics.ListAPIView):
    model = Willingness
    serializer_class = WillingnessSerializer
    permission_classes = [
        permissions.AllowAny
    ]
    
    def get_queryset(self):
        queryset = super(PartyWillingnessList, self).get_queryset()
        return queryset.filter(party__pk=self.kwargs.get('pk'))

class UserPartyList(generics.ListAPIView):
    model = Party
    serializer_class = PartySerializer
    permission_classes = [
        permissions.AllowAny
    ]
    
    def get_queryset(self):
        queryset = super(UserPartyList, self).get_queryset()
        return queryset.filter(author__username=self.request.user.username)

class MessageList(generics.ListCreateAPIView):
    model = Message
    serializer_class = MessageSerializer
    permission_classes = [
        permissions.AllowAny
    ]
    
    def pre_save(self, obj):
        obj.author = self.request.user
        return super(MessageList, self).pre_save(obj)
    
class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Message
    serializer_class = MessageSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class UserMessageList(generics.ListAPIView):
    model = Message
    serializer_class = MessageSerializer
    permission_classes = [
        permissions.AllowAny
    ]
    
    def get_queryset(self):
        queryset = super(UserMessageList, self).get_queryset()
        return queryset.filter(author__username=self.request.user.username)

class WillingnessList(generics.ListCreateAPIView):
    model = Willingness
    serializer_class = WillingnessSerializer
    permission_classes = [
        permissions.AllowAny
    ]
    
    def pre_save(self, obj):
        obj.author = self.request.user
        return super(WillingnessList, self).pre_save(obj)
    
class WillingnessDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Willingness
    serializer_class = WillingnessSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class UserWillingnessList(generics.ListAPIView):
    model = Willingness
    serializer_class = WillingnessSerializer
    permission_classes = [
        permissions.AllowAny
    ]
    
    def get_queryset(self):
        queryset = super(UserWillingnessList, self).get_queryset()
        return queryset.filter(author__username=self.request.user.username)
