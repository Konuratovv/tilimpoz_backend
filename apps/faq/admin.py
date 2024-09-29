from django.contrib import admin
from .models import Faq

from unfold.admin import ModelAdmin

@admin.register(Faq)
class FAQModel(ModelAdmin):
    pass
