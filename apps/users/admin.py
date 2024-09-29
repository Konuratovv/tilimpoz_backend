from django.contrib import admin
from .models import CustomUser

from unfold.admin import ModelAdmin

@admin.register(CustomUser)
class CustomUserAdmin(ModelAdmin):
    list_display = ('email', 'username', 'is_staff', 'is_superuser', 'points')
    search_fields = ('email', 'username')
    list_filter = ('is_staff', 'is_superuser', )
    fields = ('email', 'username', 'password', 'is_staff', 'is_superuser', 'points')
    readonly_fields = ('last_login', )

