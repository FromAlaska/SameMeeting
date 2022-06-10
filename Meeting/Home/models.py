from django.db import models

# Create your models here.
class Meeting(models.Model):
	meeting_name = models.CharField(max_length=255)
	meeting_count = models.IntegerField(default=1)
