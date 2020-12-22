from django.contrib import admin
from .models import *


admin.site.register(Student)
admin.site.register(StudentClassInfo)
# admin.site.register(StudentAdmin)

# class StudentAdmin(admin.ModelAdmin):
# 	list_display = ['students', 'age', 'class', 'status',]