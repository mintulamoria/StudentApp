from django.urls import path
from . import views
from .views import Student

app_name = 'studentapp'

urlpatterns = [
	path('', views.student_new, name='student_list'),
	path('', views.Student, name='student'),
	path('student/<int:pk>/', views.student_details, name='student_details'),
]