from django.shortcuts import render, get_object_or_404, redirect
from .forms import StudentForm
from .models import Student
from django.urls import reverse


def student_new(request):
	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			# student = form.save(commit=False)
			# student.name = request.name
			# student.published_date = timezone.now()
			# student.slug = student.name
			# student.status = 'published'
			form.save()
#			return redirect('student_list', pk=student.pk)
	else:
		form = StudentForm()
	students = Student.objects.filter(status='active').order_by('name')
#	students = Student.objects.filter(published=True).order_by('name')
	return render(request, 'studentapp/student_list.html', {'form':form, 'students':students})

def student_edit(request, pk):
    student_edit = Student.objects.get(id=pk)
    edit_forms = CreateStudent(instance=student_edit)

    if request.method == "POST":
        edit_forms = CreateStudent(request.POST, instance=student_edit)

        if edit_forms.is_valid():
            edit_forms.save()
            messages.success(request, "Edit Student Info Successfully!")
            return redirect("student_list")

    context = {
        "edit_forms": edit_forms
    }
    return render(request, "students/student_edit.html", context)

