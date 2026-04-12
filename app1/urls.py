from django.urls import path
from .views import *

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('department/', DepartmentView.as_view(), name='department'),
    path('delete-dept/<int:id>/', DeleteDepartment.as_view(), name='delete_dept'),

    path('teacher/', TeacherView.as_view(), name='teacher'),
    path('delete-teacher/<int:id>/', DeleteTeacher.as_view()),

    path('student/', StudentView.as_view(), name='student'),
    path('delete-student/<int:id>/', DeleteStudent.as_view()),

    path('update-teacher/<int:id>/', UpdateTeacher.as_view(), name='update_teacher'),
    path('update-student/<int:id>/', UpdateStudent.as_view(), name='update_student'),
]