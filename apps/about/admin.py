from django.contrib import admin
from .models import About
from unfold.admin import ModelAdmin

@admin.register(About)
class AboutAdmin(ModelAdmin):
    pass
