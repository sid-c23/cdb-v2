from . import models, serializers
from rest_framework import viewsets

class ClubViewSet(viewsets.ModelViewSet):
	queryset = models.Club.objects.all()
	serializer_class = serializers.ClubSerializer

class AnnouncementViewSet(viewsets.ModelViewSet):
	queryset = models.Announcement.objects.all()
	serializer_class = serializers.AnnouncementSerializer