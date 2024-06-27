from django.urls import path
from . import views

urlpatterns = [
    path('', views.TilibizdeListCreateAPIView.as_view(), name='tilibizde-list-create'),
]