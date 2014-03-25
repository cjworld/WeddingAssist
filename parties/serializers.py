from rest_framework import serializers
from .models import User, Party, Photo, Message, ParticipationWillingness

class UserSerializer(serializers.ModelSerializer):
	#parties = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='party-detail', lookup_field='author', required=False)
	parties = serializers.RelatedField(many=True)
	
	class Meta:
		model = User
		fields = ('id', 'username', 'first_name', 'last_name', 'parties', )
	
class PhotoSerializer(serializers.ModelSerializer):
	#serializer = PhotoSerializer(data=request.DATA, files=request.FILES)
	#image = serializers.Field('image.url')

	def get_validation_exclusions(self):
		# Need to exclude `author` since we'll add that later based off the request
		exclusions = super(PhotoSerializer, self).get_validation_exclusions()
		return exclusions + ['author']
	
	class Meta:
		model = Photo
		fields = ('id', 'title', 'image', )
		
class MessageSerializer(serializers.ModelSerializer):
	author = UserSerializer(required=False)
	
	def get_validation_exclusions(self):
		# Need to exclude `author` since we'll add that later based off the request
		exclusions = super(MessageSerializer, self).get_validation_exclusions()
		return exclusions + ['author']
	
	class Meta:
		model = Message
		fields = ('id', 'datetime', 'body', 'party', )
		
class PartySerializer(serializers.ModelSerializer):
	author = UserSerializer(required=False)
	#messages = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='parties:message-detail', required=False)
	#participationwillingnesses = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='parties:participationwillingness-detail', required=False)
	#photos = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='photo-detail', required=False)
	messages = serializers.RelatedField(many=True, read_only=True, required=False)
	participationwillingnesses = serializers.RelatedField(many=True, read_only=True, required=False)
	photos = serializers.RelatedField(many=True)

	def get_validation_exclusions(self):
		# Need to exclude `author` since we'll add that later based off the request
		exclusions = super(PartySerializer, self).get_validation_exclusions()
		return exclusions + ['author']
	
	class Meta:
		model = Party
		fields = ('id', 'datetime', 'title', 'subscription', 'date', 'time', 'place', 'photos', 'messages', 'participationwillingnesses')

	
class ParticipationWillingnessSerializer(serializers.ModelSerializer):
	author = UserSerializer(required=False)

	def get_validation_exclusions(self):
		# Need to exclude `author` since we'll add that later based off the request
		exclusions = super(ParticipationWillingnessSerializer, self).get_validation_exclusions()
		return exclusions + ['author']
	
	class Meta:
		model = ParticipationWillingness
		fields = ('id', 'participation', 'invitation', 'host', 'vegetarian', 'party', )