from django.contrib import admin
from .models import Video

admin.site.unregister(Video)
