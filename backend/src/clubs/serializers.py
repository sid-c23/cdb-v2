from rest_framework import serializers
from . import models
from .models import Announcement

class ClubSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Club
		fields = ('url', 'name', 'owner', 'description', 'members', 'location', 'announcement_set',)

class AnnouncementSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Announcement
		fields = ('url', 'club', 'author', 'text',)