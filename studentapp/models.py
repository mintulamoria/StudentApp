from django.db import models
from django.conf import settings
from django.utils import timezone



class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager,self).get_queryset().filter(status='published')

class StudentClassInfo(models.Model):
	class_name = models.IntegerField()
	class_short_form = models.CharField(max_length=10)

	def __str__(self):
		return self.class_name


# class StudentSectionInfo(models.Model):
# 	section_name = models.CharField(max_length=20)

# 	def __str__(self):
# 		return self.section_name

class Student(models.Model):
	STATUS_CHOICES = (
		('draft', 'Draft'),
		('active', 'Active'),
	)
	name = models.CharField(max_length=100)
	age = models.IntegerField()
	gender_choice = (
			("male", "Male"), 
			("female", "Female"),
	)
	gender = models.CharField(choices=gender_choice, max_length=10)
	class_type = models.ForeignKey(StudentClassInfo, on_delete=models.CASCADE)
	father_name = models.CharField(max_length=100)
	mother_name = models.CharField(max_length=100)
	address = models.TextField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	published_date = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	# class Meta: 
	# 	ordering = ('-publish',)

	class Meta:
		unique_together = ('name', 'father_name', 'mother_name',)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('student_detail',kwargs={'slug':str(self.slug)})