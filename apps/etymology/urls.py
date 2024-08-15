from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.EtymologyViewSet.as_view(), name='etymology-view'),
    path('<int:pk>', views.EtymologyDetailedAPIView.as_view(), name='etymology-detailed')
]
