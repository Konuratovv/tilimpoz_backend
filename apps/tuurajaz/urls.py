from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.TuuraJazListAPIView.as_view(), name='etymology-view'),
    path('<int:pk>', views.TuuraJazDetailedAPIView.as_view(), name='etymology-detailed')
]
