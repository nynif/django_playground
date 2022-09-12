from django.db import models

# Create your models here.
class People(models.Model):
	f_name = models.CharField(max_length=200)
	l_name = models.CharField(max_length=200)
	bio = models.TextField()
	main_picture = models.ImageField(upload_to='static/people')

	def __str__(self):
		return self.f_name + ' ' + self.l_name