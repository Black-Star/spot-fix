
from listings.views import SpotFixList, LocationList
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'spot-fix', SpotFixList)
router.register(r'location', LocationList)

urlpatterns = router.urls
