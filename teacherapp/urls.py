from django.urls import path
from . import views
from .views import Teacher

app_name = 'teacherapp'

urlpatterns = [
	path('', views.teacher_new, name='teacher_list'),
	path('', views.Teacher, name='teacher'),
]