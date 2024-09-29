from django.contrib import admin
from .models import Team

from unfold.admin import ModelAdmin

@admin.register(Team)
class TeamAdmin(ModelAdmin):
    pass