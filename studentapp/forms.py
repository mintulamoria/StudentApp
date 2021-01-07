from django import forms
from django.contrib import admin
from .models import Student


class StudentForm(forms.ModelForm):

	class Meta:
		model = Student
		fields = ('name', 'father_name', 'mother_name', 'cover', 'dob', 'age', 'class_type', 'gender', 'status', 'address')
