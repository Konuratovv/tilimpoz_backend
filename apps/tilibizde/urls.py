from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.TilibizdeCardsAPIView.as_view(), name='tilibizde-view'),
    path('<int:pk>', views.TilibizdeDetailedAPIView.as_view(), name='tilibizde-detailed')
]
