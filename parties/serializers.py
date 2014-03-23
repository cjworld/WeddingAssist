from rest_framework import serializers
from .models import User, Party, Photo, Message, ParticipationWillingness

class UserSerializer(serializers.ModelSerializer):
	parties = serializers.HyperlinkedIdentityField('parties', view_name='userparty-list', lookup_field='username')
	
	class Meta:
		model = User
		fields = ('id', 'username', 'first_name', 'last_name', 'parties', )
	
class PhotoSerializer(serializers.ModelSerializer):
    image = serializers.Field('image.url')

    def get_validation_exclusions(self):
        # Need to exclude `author` since we'll add that later based off the request
        exclusions = super(PostSerializer, self).get_validation_exclusions()
        return exclusions + ['author']
	
    class Meta:
        model = Photo
		
class MessageSerializer(serializers.ModelSerializer):
	author = UserSerializer(required=False)
	
    def get_validation_exclusions(self):
        # Need to exclude `author` since we'll add that later based off the request
        exclusions = super(PostSerializer, self).get_validation_exclusions()
        return exclusions + ['author']
	
    class Meta:
        model = Message
		fields = ('id', 'author', 'datetime', 'body', 'party', )
		
class PartySerializer(serializers.ModelSerializer):
	author = UserSerializer(required=False)
	messages = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='message-detail', required=False)
	participationwillingnesses = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='participationwillingness-detail', required=False)
	photos = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='photo-detail', required=False)

    def get_validation_exclusions(self):
        # Need to exclude `author` since we'll add that later based off the request
        exclusions = super(PostSerializer, self).get_validation_exclusions()
        return exclusions + ['author']
	
    class Meta:
        model = Party
		fields = ('id', 'author', 'datetime', 'title', 'subscription', 'date', 'time', 'place', 'photos', 'messages', 'participationwillingnesses')

	
class ParticipationWillingnessSerializer(serializers.ModelSerializer):
	author = UserSerializer(required=False)

    def get_validation_exclusions(self):
        # Need to exclude `author` since we'll add that later based off the request
        exclusions = super(PostSerializer, self).get_validation_exclusions()
        return exclusions + ['author']
	
    class Meta:
        model = ParticipationWillingness
		fields = ('id', 'author', 'participation', 'invitation', 'host', 'vegetarian', 'party', )