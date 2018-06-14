from django.conf.urls import url
from . import views

app_name='items'

import time
urlpatterns = [

	url('',views.index,name='index'),
	url('create/',views.create,name='create'),
	url('<itemname>/',views.detail,name='detail'),



]