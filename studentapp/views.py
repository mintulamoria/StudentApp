from django.shortcuts import render, get_object_or_404, redirect
from .forms import StudentForm
from .models import Student


def student_new(request):
	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = StudentForm()
	students = Student.objects.all().order_by('name')
	return render(request, 'studentapp/student_list.html', {'form':form, 'students':students})