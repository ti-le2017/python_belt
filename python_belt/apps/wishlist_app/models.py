from __future__ import unicode_literals

from django.db import models
from ..login_app.models import *

class ItemManager(models.Manager):
	def basic_validation(self, postData):
		errors = {}
		if len(postData['item']) < 3:
			errors['item'] = "Must contain atleast three Character"
		if len(postData['item']) == 0:
			errors['empty_item'] = "Textbox cannot be empty"		
		return errors	


class Item(models.Model):
	item = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	liked_users = models.ManyToManyField(User, related_name='liked_items')
	user = models.ForeignKey(User, related_name="item")

	def __repr__(self):
		return "<Item object: {} {} {}".format(self.id, self.item, self.created_at)

	objects = ItemManager()
