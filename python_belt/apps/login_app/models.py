from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
	def basic_validator(self, postData):
		errors = {}
		if len(postData['name']) < 2:
			errors['name'] = "Name must be atleast two characters"
		if len(postData['user_name']) < 2:
			errors['user_name'] = "Name must be atleast two characters"
		if len(postData['password']) != len(postData['confirm_password']):
			errors['password'] = "Password does not match"
		if len(postData['password']) < 8:
			errors['password_len'] = "Password must be atleast 8 characters long"
		if len(postData['confirm_password']) < 8:
			errors['confirm_password'] = "Password must be atleast 8 characters long"
		return errors

	def login(self, postData):
		user_login = {}
		user = User.objects.filter(user_name=postData['user_name']) 
		if len(user) > 0 and user[0].password == postData['password_login']:
			user_login['access'] = True
			user_login['user_id'] = user[0].id
		else:
			user_login['error'] = "Your Email and Password login is incorrect. Please try again."
			user_login['access'] = False
		return user_login

class User(models.Model):
    name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=100)
    date_hired = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
