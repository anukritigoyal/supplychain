from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
	url('create/',views.item_create.as_view()),
	url('history/',views.user_history.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)