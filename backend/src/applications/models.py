from django.db import models
from users.models import CustomUser
from clubs.models import Club

class Application(models.Model):
	APPLICATION_CHOICES = (
		('ACC', 'Accepted'),
		('REJ', 'Rejected'),
		('INP', 'In Progress'),
		('INC', 'Incomplete'),
		('COM', 'Complete'),
	)
	club = models.ForeignKey(Club, on_delete=models.CASCADE)
	applicant = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	status = models.CharField(max_length=3, choices=APPLICATION_CHOICES, default='INC')

class Entry(models.Model):
	question = models.CharField(max_length=300)
	answer = models.TextField(blank=True, null=True)
	# applicant = models.
