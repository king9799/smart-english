from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth import views 
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Timetable, Salary, Building, Staff, Other, Room, Student
from. models import Subjects, Group, LessonType, Patterns

@login_required
def dashboard(request):
	return render(request,'dashboard.html',{'section': 'dashboard'})

def config(request):
	return render(request, 'config.html')

def time(request):
	courses = Timetable.objects.all
	return render(request, 'time.html', {'courses':courses})

def building(request):
	buildings = Building.objects.all()
	return render(request, 'building.html', {'buildings':buildings})

def room(request):
	rooms = Room.objects.all()
	return render(request, 'room.html', {'rooms':rooms})

def register(request):
	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)
		if user_form.is_valid():
			new_user = user_form.save(commit=False)
			new_user.set_password(
				user_form.cleaned_data['password']
			)
			new_user.save()
			UserProfile.objects.create(user=new_user)
			return render(request, 'register_done.html',
			{'new_user':new_user})
	else:
		user_form = UserRegistrationForm()
	return render(request, 'register.html',
	{'user_form':user_form})

@login_required
def edit(request):
	if request.method == 'POST':
		user_form = UserEditForm(instance=request.user,
		data=request.POST)
		profile_form = ProfileEditForm(
			instance=request.user.profile,
			data=request.POST,
			files=request.FILES
		)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
	else:
		user_form = UserEditForm(instance=request.user)
		profile_form = ProfileEditForm(instance=request.user.profile)
	return render(request, 'edit.html', {'user_form':user_form, 'profile_form':profile_form})


def profile(request):
	user = request.user
	return render(request, 'profile.html', {'user':user})

def teacher(request):
	teachers = Staff.objects.all()
	return render(request, 'teacher.html', {'teachers':teachers})

def salary(request):
	salary = Salary.objects.all()
	return render(request, 'salary.html', {'salary':salary})

def other(request):
	extra_details = Other.objects.all()
	return render(request, 'other.html', {'extra_details':extra_details})

def student(request):
	students = Student.objects.all()
	return render(request, 'student.html', {'students':students})

def modal_time(request):
	subjects = Subjects.objects.all()
	groups = Group.objects.all()
	lesson_types = LessonType.objects.all()
	lesson_patterns = Patterns.objects.all()
	return render(request, 'modal_time.html', 
	{'subjects':subjects, 'groups':groups, 'lesson_types':lesson_types,
	'lesson_patterns':lesson_patterns})