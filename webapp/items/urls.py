from django.conf.urls import url
from django.urls import path
from . import views

app_name='items'

import time
urlpatterns = [

	url('',views.index,name='index'),
	url('create/',views.create,name='create'),
	path('<str:itemname>/',views.detail,name='detail'),



]