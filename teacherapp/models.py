from django.db import models
from django.utils import timezone
from django.conf import settings

class TeacherDeptInfo(models.Model):
	dept_name = models.CharField(max_length=50)

	def __str__(self):
		return self.dept_name

class TeacherSubInfo(models.Model):
	sub_name = models.CharField(max_length=50)

	def __str__(self):
		return self.sub_name

class TimestampedModel(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class meta:
		abstract = True

class Teacher(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(unique=True)
	age = models.IntegerField()
	cover = models.ImageField(upload_to='images/', blank=True)
	gender_choice = (
		("Male", "Male"),
		("Female", "Female"),
	)
	gender = models.CharField(choices=gender_choice, max_length=10)
	joining_date = models.DateField()
	dept_type = models.ForeignKey(TeacherDeptInfo, on_delete=models.CASCADE)
	sub_type = models.ForeignKey(TeacherSubInfo, on_delete=models.CASCADE)
	salary = models.IntegerField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name