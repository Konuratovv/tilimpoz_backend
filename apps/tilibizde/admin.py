from django.contrib import admin
from django.db import models

from .models import Tilibizde

from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget

@admin.register(Tilibizde)
class TilibizdeAdmin(ModelAdmin):
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }
