from django.contrib import admin
from .models import Book, BookCategory

from unfold.admin import ModelAdmin

@admin.register(Book)
class BookAdmin(ModelAdmin):
    pass

@admin.register(BookCategory)
class BookCategoryAdmin(ModelAdmin):
    pass