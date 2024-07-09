"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .schema_urls import urlpatterns as schema_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('apps.users.urls')),
    path('api/rule/', include('apps.rules.urls')),
    path('api/etymology/', include('apps.etymology.urls')),
    path('api/tilibizde/', include('apps.tilibizde.urls')),
    path('api/documents/', include('apps.documents.urls')),
    path('api/books/', include('apps.books.urls')),
    path('api/categories/', include('apps.categories.urls')),
    path('api/sozduk/', include('apps.sozduk.urls')),
    path('api/about/', include('apps.about.urls')),
    path('api/faq/', include('apps.faq.urls')),
    path('api/qa/', include('apps.qa.urls')),
    path('api/contacts/', include('apps.contacts.urls')),
    path('api/team/', include('apps.team.urls')),
]

urlpatterns += schema_urls