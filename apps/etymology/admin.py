from django.contrib import admin
from django.db import models

from .models import Etymology

from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget

@admin.register(Etymology)
class EtymologyAdmin(ModelAdmin):
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }