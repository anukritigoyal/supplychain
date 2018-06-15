from django.conf.urls import url
from django.urls import path
from . import views

app_name='items'

import time
urlpatterns = [
	
	url('home/',views.index,name='index'),
	url('login/',views.UserFormView.as_view(),name= 'login'),
	url('create/',views.create,name='create'),
	path('details/<itemname>/',views.detail,name='detail'),
	path('details/<itemname>/checks/',views.checked , name = 'checked')
	url('map/',views.map,name='map')

]