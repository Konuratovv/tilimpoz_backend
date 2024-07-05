from rest_framework.routers import DefaultRouter
from .views import TilibizdeViewSet

router = DefaultRouter()
router.register(r'', TilibizdeViewSet)

urlpatterns = router.urls