from django.urls import path
from django.conf.urls import url

from . import views
app_name = 'ptypes'

urlpatterns = [
    url('index/', views.index, name='index'),
    url('create/', views.create, name='create'),
    url('details/<ptype_name>', views.details, name='details'),
] 