from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.SabattuuJoobtorListAPIView.as_view(), name='sabattuu-joobtor-view'),
    path('<int:pk>', views.SabattuuJoobtorDetailedAPIView.as_view(), name='sabattuu-joobtor-detailed')
]
