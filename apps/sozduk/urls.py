from rest_framework.routers import DefaultRouter
from .views import SozdukViewSet

router = DefaultRouter()
router.register(r'', SozdukViewSet)

urlpatterns = router.urls