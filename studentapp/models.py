from django.db import models
from django.conf import settings
from django.utils import timezone
#from model_utils import FieldTracker



class Student(models.Model):
	STATUS_CHOICES = (
		('draft', 'Draft'),
		('published', 'Published'),
	)
	name = models.CharField(max_length=100)
	father_name = models.CharField(max_length=100)
	mother_name = models.CharField(max_length=100)
	address = models.TextField(max_length=200)
	created_date = models.DateTimeField(auto_now_add=True)
	published_date = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, 
                              choices=STATUS_CHOICES,
                              default='draft')

	
	class Meta: 
		ordering = ('-publish',)

	class Meta:
		unique_together = ('name', 'father_name', 'mother_name',)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.name