from django.db import models

# Create your models here.
class Book(models.Model):
	name = models.CharField(max_length=200)
	todo = models.BooleanField()

	def __str__(self):
		return self.name