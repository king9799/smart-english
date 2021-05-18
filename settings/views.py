from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth import views 
from django.contrib.auth.decorators import login_required
from .models import Profile


# def index(request):
# 	return render(request, 'index.html')

@login_required
def dashboard(request):
	return render(request,'dashboard.html',{'section': 'dashboard'})



def config(request):
	return render(request, 'config.html')

def time(request):
	return render(request, 'time.html')

def building(request):
	return render(request, 'building.html')

def room(request):
	return render(request, 'room.html')

def register(request):
	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)
		if user_form.is_valid():
			new_user = user_form.save(commit=False)
			new_user.set_password(
				user_form.cleaned_data['password']
			)
			new_user.save()
			Profile.objects.create(user=new_user)
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