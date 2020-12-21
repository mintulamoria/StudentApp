from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

	class Meta:
		model = Student
		fields = ('name', 'father_name', 'mother_name', 'age', 'class_type', 'gender', 'address',)

		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
			'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
			'gender': forms.Select(attrs={'class': 'form-control'}),
			'class_type': forms.Select(attrs={'class': 'form-control'}),
			'fathers_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fathers Name'}),
			'mothers_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mothers Name'}),
		}