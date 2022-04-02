from django.db import models

# Create your models here.
class Contact(models.Model):
	full_name = models.CharField(max_length=256)
	relationship = models.CharField(max_length=256)
	email = models.EmailField()
	phone_number = models.CharField(max_length=12)
	address = models.CharField(max_length=256)

	def __str__(self):
		return self.full_name