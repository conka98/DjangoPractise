from django.shortcuts import render
from .forms import UserForm, UserProfileInfoForm




#
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
	dict = {'text':'hellooooooo there!!!' , 'number':100}
	return render(request , 'basicApp/index.html',context = dict)

def other(request):
	return render(request , 'basicApp/other.html')

def relative_url_templates(request):
	return render(request, 'basicApp/relative_url_templates.html')


@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse("login"))


def index1(request):
	return render(request,'basicApp/index1.html')


def register(request):
	registered = False

	if request.method == "POST":
		user_form = UserForm(data = request.POST)
		profile_form = UserProfileInfoForm(data = request.POST)

		if user_form.is_valid() and profile_form.is_valid():

			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			if 'profile_pic' in request.FILES:
				profile.profile_pic = request.FILES['profile_pic']

			profile.save()

			registered = True
		else:
			print(user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileInfoForm()


	return render(request, 'basicApp/registration.html',{
		'registered':registered,
		'user_form':user_form,
		'profile_form':profile_form
		})



def user_login(request):
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")

		user = authenticate(username=username,password=password)

		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect(reverse("index1"))

			else:
				return HttpResponse("user is not active")
		else:
			print("Login Failed")
			print("username :{} password:{}".format(username,password))

			return HttpResponse("Invalid Login details")	
	else:
		return render(request,'basicApp/login.html',{})