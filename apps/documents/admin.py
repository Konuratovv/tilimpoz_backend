from django.contrib import admin
from .models import Document

from unfold.admin import ModelAdmin

@admin.register(Document)
class DocumentAdmin(ModelAdmin):
    pass