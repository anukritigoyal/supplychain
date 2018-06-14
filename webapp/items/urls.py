from django.conf.urls import url
from . import views

app_name='items'

import time
urlpatterns = [

	url('',views.index,name='index'),
#	url('<str:itemname>/',views.detail,name='detail'),


]