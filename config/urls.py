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
from django.views.generic import RedirectView


from .schema_urls import urlpatterns as schema_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path('api/v1/', include([
            path('users/', include('apps.users.urls')),
            path('rule/', include('apps.rules.urls')),
            path('etymology/', include('apps.etymology.urls')),
            path('tilibizde/', include('apps.tilibizde.urls')),
            path('documents/', include('apps.documents.urls')),
            path('books/', include('apps.books.urls')),
            path('categories/', include('apps.categories.urls')),
            path('sozduk/', include('apps.sozduk.urls')),
            path('about/', include('apps.about.urls')),
            path('faq/', include('apps.faq.urls')),
            path('qa/', include('apps.qa.urls')),
            path('contacts/', include('apps.contacts.urls')),
            path('team/', include('apps.team.urls')),
            path('videos/', include('apps.videos.urls')),
            path('news/', include('apps.news.urls')),
            path('quiz/', include('apps.quiz.urls')),
            path('sabattuu-joobtor/', include('apps.sj.urls')),
            path('tuura-jaz/', include('apps.tuurajaz.urls')),
])),
    path('', RedirectView.as_view(url='/swagger/')),
]

urlpatterns += schema_urls