from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login

from .models import Department, Teacher, Student
from .forms import DepartmentForm, TeacherForm, StudentForm, RegisterForm


# 🔐 Login View
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        u = request.POST.get('username')
        p = request.POST.get('password')

        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            return redirect('dashboard')
        return render(request, 'login.html')


# 📝 Register View
class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
        return render(request, 'register.html', {'form': form})


# 📊 Dashboard
class DashboardView(View):
    def get(self, request):
        return render(request, 'dashboard.html')


# 🏢 Department
class DepartmentView(View):
    def get(self, request):
        data = Department.objects.all()
        form = DepartmentForm()
        return render(request, 'department.html', {'data': data, 'form': form})

    def post(self, request):
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('department')


# 🔐 Delete Department (with password)
from django.shortcuts import get_object_or_404

class DeleteDepartment(View):
    def get(self, request, id):
        dept = get_object_or_404(Department, id=id)
        return render(request, 'delete_department.html', {'dept': dept})

    def post(self, request, id):
        dept = get_object_or_404(Department, id=id)
        password = request.POST.get('password')

        if password == "admin123":
            dept.delete()
            return redirect('department')

        return render(request, 'delete_department.html', {
            'dept': dept,
            'error': 'Wrong Password'
        })


# 👨‍🏫 Teacher
class TeacherView(View):
    def get(self, request):
        data = Teacher.objects.all()
        form = TeacherForm()
        return render(request, 'teacher.html', {'data': data, 'form': form})

    def post(self, request):
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('teacher')


class DeleteTeacher(View):
    def post(self, request, id):
        Teacher.objects.get(id=id).delete()
        return redirect('teacher')


# 🎓 Student
class StudentView(View):
    def get(self, request):
        data = Student.objects.all()
        form = StudentForm()
        return render(request, 'student.html', {'data': data, 'form': form})

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('student')


class DeleteStudent(View):
    def post(self, request, id):
        Student.objects.get(id=id).delete()
        return redirect('student')
    

class UpdateTeacher(View):
    def get(self, request, id):
        teacher = get_object_or_404(Teacher, id=id)
        form = TeacherForm(instance=teacher)
        return render(request, 'update_teacher.html', {'form': form})

    def post(self, request, id):
        teacher = get_object_or_404(Teacher, id=id)
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher')
        return render(request, 'update_teacher.html', {'form': form})
    


class UpdateStudent(View):
    def get(self, request, id):
        student = get_object_or_404(Student, id=id)
        form = StudentForm(instance=student)
        return render(request, 'update_student.html', {'form': form})

    def post(self, request, id):
        student = get_object_or_404(Student, id=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student')
        return render(request, 'update_student.html', {'form': form})