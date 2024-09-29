from django.contrib import admin
from django.db import models

from .models import SabattuuModel

from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget

# Register your models here.

@admin.register(SabattuuModel)
class SabattuuAdmin(ModelAdmin):
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }
