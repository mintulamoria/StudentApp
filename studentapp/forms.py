from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

	class Meta:
		model = Student
		fields = ('name', 'father_name', 'mother_name')