from django.contrib import admin
from unfold.admin import ModelAdmin

from . import models

# Register your models here.

@admin.register(models.Partner)
class PartnersAdmin(ModelAdmin):
    pass

