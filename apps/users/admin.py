from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'is_staff', 'is_superuser', 'is_verified', 'points')
    search_fields = ('email', 'username')
    list_filter = ('is_staff', 'is_superuser', 'is_verified')

