from django.contrib import admin
from .models import TuuraJazModel

from unfold.admin import ModelAdmin

@admin.register(TuuraJazModel)
class TuuraJazAdmin(ModelAdmin):
    pass