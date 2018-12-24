from . import models, serializers
from rest_framework import viewsets

class CustomUserViewSet(viewsets.ModelViewSet):
	queryset = models.CustomUser.objects.all()
	serializer_class = serializers.CustomUserSerializer