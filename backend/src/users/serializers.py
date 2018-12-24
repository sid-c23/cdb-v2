from rest_framework import serializers
from . import models

class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.CustomUser
		fields = ('url', 'username', 'email', 'club_set')