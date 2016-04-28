from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from listings import views
urlpatterns = [
    url(r'^spot-fix/$', views.SpotFixList.as_view()),
    url(r'^', views.index),
]

urlpatterns = format_suffix_patterns(urlpatterns)
