from django.shortcuts import render, get_object_or_404, redirect
from .models import Teacher
from .forms import TeacherForm
from django.contrib import messages
from django.core.paginator import Paginator


# def teacher_list(request):
# 	teachers = TeacherInfo.object.all()
# 	paginator = Paginator(teachers, 1)


def teacher_new(request):
	if request.method == 'POST':
		form = TeacherForm(request.POST)
		if form.is_valid():
			teacher = form.save(commit=False)
			teacher.author = request.teacher
			teacher.published_date = timezone.now()
			teacher.slug = teacher.name
			teacher.status = 'published'
			form.save()
			return redirect('teacher_details', pk=teacher.pk)
	else:
		form = TeacherForm()
	teachers = Teacher.objects.all().order_by('name')
	return render(request, 'teacherapp/teacher_list.html', {'form':form, 'teachers':teachers})



# Create your views here.
