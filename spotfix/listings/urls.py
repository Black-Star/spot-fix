
from listings.views import SpotFixList
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'spot-fix', SpotFixList)

urlpatterns = router.urls
