from django.db import models
from users.models import CustomUser

class Club(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField()
	owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="clubs_created")
	members = models.ManyToManyField(CustomUser, blank=True)
	location = models.CharField(max_length=50, null=True, blank=True)

	def __str__(self):
		return self.name

class Announcement(models.Model):
	club = models.ForeignKey(Club, on_delete=models.CASCADE)
	text = models.TextField()
	author = models.ForeignKey(CustomUser, on_delete=models.SET_DEFAULT, default="Anonymous")

	def __str__(self):
		return self.author + "-" + self.club
