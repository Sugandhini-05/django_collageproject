from django.contrib import admin
from .models import Department, Teacher, Student


# Department Admin
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code']
    search_fields = ['name', 'code']


# Teacher Admin
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'department']
    search_fields = ['name', 'email']
    list_filter = ['department']


# Student Admin
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll_no', 'department']
    search_fields = ['name', 'roll_no']
    list_filter = ['department']


# Register Models
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)