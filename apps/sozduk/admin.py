from django.contrib import admin
from .models import Sozduk, SozdukCategory

from unfold.admin import StackedInline, ModelAdmin

class SozInline(StackedInline):
    model = Sozduk
    extra = 1

@admin.register(SozdukCategory)
class SoadukCategoryAdmin(ModelAdmin):
    inlines = (SozInline, )
