from django.shortcuts import render, get_object_or_404, redirect
from .models import Teacher
from .forms import TeacherForm
from django.contrib import messages
from django.core.paginator import Paginator


def teacher_new(request):
	if request.method == 'POST':
		form = TeacherForm(request.POST)
		if form.is_valid():
			form.save()
			# return redirect('teacher_details', pk=teacher.pk)
	else:
		form = TeacherForm()
	teachers = Teacher.objects.all().order_by('name')
	return render(request, 'teacherapp/teacher_list.html', {'form':form, 'teachers':teachers})