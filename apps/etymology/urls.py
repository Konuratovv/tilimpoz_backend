# etymology/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.EtymologyListCreateAPIView.as_view(), name='etymology-list-create'),
]

