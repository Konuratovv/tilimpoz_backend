from rest_framework.routers import DefaultRouter
from .views import RuleViewSet, RuleCardViewSet

router = DefaultRouter()
router.register(r'rules', RuleViewSet)
router.register(r'rulecards', RuleCardViewSet)

urlpatterns = router.urls
