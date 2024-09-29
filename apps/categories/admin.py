from django.contrib import admin
from .models import Category

from unfold.admin import ModelAdmin

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    pass