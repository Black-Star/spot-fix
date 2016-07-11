from rest_framework import routers
from django.conf.urls import url, include
from listings import views

router = routers.SimpleRouter()
router.register(r'spot-fix', views.SpotFixList)
router.register(r'location', views.LocationList)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', views.index)
]
