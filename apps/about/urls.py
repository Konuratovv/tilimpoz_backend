# apps/about/urls.py
from rest_framework.routers import DefaultRouter
from .views import AboutViewSet

router = DefaultRouter()
router.register(r'', AboutViewSet)

urlpatterns = router.urls

