from rest_framework import serializers
from hannuri.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'generation' ,'color','is_staff']

class SessionSerializerForSeason(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['id', 'week', 'title']


class SeasonSerializer(serializers.ModelSerializer):
    session = SessionSerializerForSeason(many=True)
    googleFolderId = serializers.ReadOnlyField()

    class Meta:
        model = Season
        fields = ['id', 'year', 'semester', 'title', 'leader', 'sessioner', 'socializer', 'session', 'googleFolderId']

class DetgoriSerializerForSession(serializers.ModelSerializer):
    authorName = serializers.ReadOnlyField(source='author.name')
    authorColor = serializers.ReadOnlyField(source='author.color')

    class Meta:
        model = Detgori
        fields = ['id', 'title', 'author', 'authorName', 'authorColor', 'googleId'] 

class SessionSerializer(serializers.ModelSerializer):
    readfile = serializers.HyperlinkedRelatedField(many=True, view_name='sessionreadfile-detail', read_only=True)
    detgori = DetgoriSerializerForSession(many=True)
    googleFolderId = serializers.ReadOnlyField()

    class Meta:
        model = Session
        fields = ['id', 'season', 'week', 'title', 'readfile', 'detgori', 'googleFolderId']

class SessionReadfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionReadfile
        fields = ['id', 'parentSession',  'googleId']

class DetgoriSerializer(serializers.ModelSerializer):
    authorId = serializers.ReadOnlyField(source='author.id')
    authorName = serializers.ReadOnlyField(source='author.name')
    authorColor = serializers.ReadOnlyField(source='author.color')
    googleId = serializers.ReadOnlyField()

    class Meta:
        model = Detgori
        fields = ['id', 'parentSession', 'title', 'authorId', 'authorColor','authorName', 'date', 'googleId',]
        

class DetgoriReadTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetgoriReadTime
        fields = '__all__'

class SentenceSerializer(serializers.ModelSerializer):
    detgori_title = serializers.ReadOnlyField(source='detgori.title')
    year = serializers.ReadOnlyField(source='detgori.parentSession.season.year')
    semester = serializers.ReadOnlyField(source='detgori.parentSession.season.semester')
    title = serializers.ReadOnlyField(source='detgori.title')
    author = serializers.ReadOnlyField(source='detgori.author.name')
    link = serializers.ReadOnlyField(source='detgori.googleId')

    class Meta:
        model = Sentence
        fields = ['id', 'detgori_title', 'content', 'year', 'semester', 'title', 'author', 'link'] 