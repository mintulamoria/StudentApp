from django.shortcuts import render, get_object_or_404, redirect
from .forms import StudentForm
from .models import Student
from django.urls import reverse


def student_new(request):
	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			student = form.save(commit=False)
			student.author = request.student
			student.published_date = timezone.now()
			student.slug = student.name
			student.status = 'published'
			form.save()
			return redirect('student_details', pk=student.pk)
	else:
		form = StudentForm()
	students = Student.objects.filter(status='active').order_by('name')
#	students = Student.objects.filter(published=True).order_by('name')
	return render(request, 'studentapp/student_list.html', {'form':form, 'students':students})