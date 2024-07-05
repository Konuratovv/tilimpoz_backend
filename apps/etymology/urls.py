from rest_framework.routers import DefaultRouter
from .views import EtymologyViewSet

router = DefaultRouter()
router.register(r'', EtymologyViewSet)

urlpatterns = router.urls

