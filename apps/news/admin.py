from django.contrib import admin
from .models import News

from unfold.admin import ModelAdmin

@admin.register(News)
class NewsAdmin(ModelAdmin):
    pass
