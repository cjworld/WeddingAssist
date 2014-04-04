from rest_framework import serializers
from .models import User, Party, Photo, Message, Willingness

class UserSerializer(serializers.ModelSerializer):
	#parties = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='party-detail', lookup_field='author', required=False)
	#parties = serializers.RelatedField(many=True)
	
	class Meta:
		model = User
		fields = ('id', 'username', 'first_name', 'last_name', )
	
class PhotoSerializer(serializers.ModelSerializer):
	#serializer = PhotoSerializer(data=request.DATA, files=request.FILES)
	author = UserSerializer(required=False)
	image = serializers.Field('image.url')

	def get_validation_exclusions(self):
		# Need to exclude `author` since we'll add that later based off the request
		exclusions = super(PhotoSerializer, self).get_validation_exclusions()
		return exclusions + ['author']
	
	class Meta:
		model = Photo
		fields = ('id', 'author', 'title', 'image', )
		
class MessageSerializer(serializers.ModelSerializer):
	author = UserSerializer(required=False)
	
	def get_validation_exclusions(self):
		# Need to exclude `author` since we'll add that later based off the request
		exclusions = super(MessageSerializer, self).get_validation_exclusions()
		return exclusions + ['author']
	
	class Meta:
		model = Message
		fields = ('id', 'author', 'datetime', 'body', 'party', )
		
class WillingnessSerializer(serializers.ModelSerializer):
	author = UserSerializer(required=False)

	def get_validation_exclusions(self):
		# Need to exclude `author` since we'll add that later based off the request
		exclusions = super(WillingnessSerializer, self).get_validation_exclusions()
		return exclusions + ['author']
	
	class Meta:
		model = Willingness
		fields = ('id', 'author', 'participation', 'invitation', 'host', 'vegetarian', 'party', )
		
class PartySerializer(serializers.ModelSerializer):
	author = UserSerializer(required=False)
	date = serializers.DateField(format="%Y-%m-%d", input_formats=["%Y-%m-%d"], required=False)
	time = serializers.TimeField(format="%H:%M:%S", input_formats=["%H:%M:%S"], required=False)
	photos = PhotoSerializer(many=True, read_only=True, required=False)

	def get_validation_exclusions(self):
		# Need to exclude `author` since we'll add that later based off the request
		exclusions = super(PartySerializer, self).get_validation_exclusions()
		return exclusions + ['author']
	
	class Meta:
		model = Party
		fields = ('id', 'author', 'datetime', 'title', 'subscription', 'date', 'time', 'place', 'photos')
		depth = 2

