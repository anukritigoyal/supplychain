from django.urls import path
from django.conf.urls import url

from . import views

# NoReverseMatch error if this line is not added
app_name = 'ptypes'

urlpatterns = [
    url('index/', views.index, name='index'),
    #url('create/', views.CreatePageView.as_view(), name='create'),
]    