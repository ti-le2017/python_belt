from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

#***************** Login Page ***********************
def index(request):
	return render(request, 'login_app/index.html')


#***************** Register User ********************
def register(request):
	# error validation
	errors = User.objects.basic_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect('/')
	else:
		# Create User
		if request.POST['password'] == request.POST['confirm_password']:
			User.objects.create(name=request.POST['name'], user_name=request.POST['user_name'], password=request.POST['password'], date_hired=request.POST['date_hired'])
		else:
			print"********************"
			print "password dont match"
			return redirect ('/')
	return redirect('/')


#***************** Validate Login ********************
def login(request):
	user_login = User.objects.login(request.POST)
	if user_login['access']:
		request.session['user_id'] = user_login['user_id']
		return redirect('/wishlist')
	else:
		for tag, error in user_login.iteritems():
			messages.error(request, error, extra_tags=tag)	#extra_tags remove the key from the dictionary in messages
		return redirect('/')







