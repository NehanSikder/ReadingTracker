from django.db import models

# Create your models here.
class Book(models.Model):
	name = models.CharField(max_length=200)
	already_read = models.BooleanField()
	user = models.CharField(max_length=200)
	completed_date_time = models.DateTimeField(null=True, blank=True) 


	def __str__(self):
		return self.name + " " + str(self.already_read)