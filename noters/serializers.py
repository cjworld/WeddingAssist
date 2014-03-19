from rest_framework import serializers
from noters.models import Memo, Notebook

class MemoSerializer(serializers.ModelSerializer):
    author = serializers.HyperlinkedRelatedField(read_only=True, required=False, view_name='users:user-detail')
    recipients = serializers.HyperlinkedRelatedField(many=True, required=False, view_name='users:user-detail')
    datetime = serializers.DateTimeField(required=False)
    notebook = serializers.HyperlinkedRelatedField(required=False, view_name='noters:notebook-detail')

    class Meta:
        model = Memo
        fields = ('author', 'recipients', 'created', 'title', 'message', 'alarm', 'datetime', 'notebook')

class NotebookSerializer(serializers.ModelSerializer):
    owner = serializers.HyperlinkedRelatedField(read_only=True, required=False, view_name='users:user-detail')
    partners = serializers.HyperlinkedRelatedField(many=True, required=False, view_name='users:user-detail')
    memos = serializers.HyperlinkedRelatedField(many=True, required=False, view_name='noters:memo-detail')
    #memos = serializers.RelatedField(read_only=True, required=False)

    class Meta:
        model = Notebook
        fields = ('title', 'subscription', 'owner', 'partners', 'memos')