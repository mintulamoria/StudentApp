from django.db import models
from django.conf import settings
from django.utils import timezone



class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager,self).get_queryset().filter(status='published')

class StudentClassInfo(models.Model):
	class_name = models.CharField(max_length=20)
	class_short_form = models.CharField(max_length=10)

	def __str__(self):
		return self.class_name


class Student(models.Model):
	STATUS_CHOICES = (
		('draft', 'Draft'),
		('active', 'Active'),
	)
	name = models.CharField(max_length=100)
#	dob = models.DateField()
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

	
	# def calculate_age(self):
	# 	today = date.today()

	# 	try: 
	# 		birthday = self.dob.replace(year=today.year)
 #        # raised when birth date is February 29 and the current year is not a leap year
	# 	except ValueError:
	# 		birthday = self.dob.replace(year=today.year, day=born.day-1)

	# 	if birthday > today:
	# 		return today.year - born.year - 1
	# 	else:
	# 		return today.year - born.year


	class Meta:
		unique_together = ('name', 'father_name', 'mother_name',)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('student_detail',kwargs={'slug':str(self.slug)})