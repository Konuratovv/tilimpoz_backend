from django.urls import path
from . import views

urlpatterns = [
    path('', views.SozdukListCreateAPIView.as_view(), name='sozduk-list-create'),
]
