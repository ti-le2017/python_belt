from django.shortcuts import render, redirect
from django.contrib import messages
from ..login_app.models import *
from .models import *


#******************* Home Page *************************************
def index(request):
	user=request.session['user_id']
	this_user=User.objects.get(id=user)

	context = {
		'this_user': this_user,
		'user_items': this_user.item.all(),
		'joined_item': Item.objects.filter(liked_users=User.objects.get(id=user)),
		'all_user': Item.objects.exclude(user=User.objects.get(id=user))
	}

	return render(request, 'wishlist_app/index.html', context)

#******************** Add Form Page ********************************
def add(request):
	return render(request, 'wishlist_app/add.html')


#********************* Add to Database *****************************
def process(request):
	user = User.objects.get(id=request.session['user_id'])

	errors= Item.objects.basic_validation(request.POST)

	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect ('/wishlist/add')
	else:
		this_item=Item.objects.create(item=request.POST['item'], user=user)

	return redirect('/wishlist')

#******************** Logout ***************************************
def logout(request):
	request.session.clear()
	return redirect('/login')


#******************** Join *****************************************
def join(request, item_id):
	this_user=User.objects.get(id=request.session['user_id'])
	this_item=Item.objects.get(id=item_id)
	this_user.liked_items.add(this_item)
	this_user.save()

	return redirect('/wishlist')

#******************** Remove User **********************************
def remove(request, item_id):
	item = Item.objects.get(id=item_id)
	user = User.objects.get(id=request.session['user_id'])
	item.liked_users.remove(user)
	item.save()

	return redirect('/wishlist')


#******************** Delete User **********************************
def delete(request, item_id):
	item = Item.objects.get(id=item_id)
	item.delete()

	return redirect('/wishlist')


#******************** Description **********************************
def likes(request, item_id):
	context = {
		'user_liked': User.objects.filter(liked_items=Item.objects.get(id=item_id))
	}

	return render(request, 'wishlist_app/likes.html', context)








