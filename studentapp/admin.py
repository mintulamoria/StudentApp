from django.contrib import admin
from .models import *


class StudentAdmin(admin.ModelAdmin):
	list_display=('name', 'father_name', 'cover', 'status',)
	search_fields=('name', 'father_name',)

	def student_cover(self):
		return '<cover src="%s"/>' % self.cover
#	student_cover.allow_tags = True


admin.site.register(Student, StudentAdmin)
admin.site.register(StudentClassInfo)