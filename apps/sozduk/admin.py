from django.contrib import admin
from .models import Sozduk, SozdukCategory

class SozInline(admin.StackedInline):
    model = Sozduk
    extra = 1

@admin.register(SozdukCategory)
class SoadukCategoryAdmin(admin.ModelAdmin):
    inlines = (SozInline, )
