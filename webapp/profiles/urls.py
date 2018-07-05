from django.conf.urls import url
from django.urls import path
from . import views

app_name='profiles'

import time
urlpatterns = [
	url('home/',views.index,name='home'),
	url('create/',views.CreateProfileView.as_view(),name='create'),
	#path('change/<username>/',views.change,name='change'),

]