from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^add$', views.add),
	url(r'^process$', views.process),
	url(r'^logout$', views.logout),
	url(r'^join/(?P<item_id>\d+)$', views.join),
	url(r'^likes/(?P<item_id>\d+)$', views.likes),
	url(r'^remove/(?P<item_id>\d+)$', views.remove),
	url(r'^delete/(?P<item_id>\d+)$', views.delete)
]