import nested_admin

from django.contrib import admin
from django.http.request import HttpRequest

from unfold.admin import StackedInline, ModelAdmin

from .models import TestCategory, Test, Question, Answer

# Register your models here.

class AnswerInline(nested_admin.NestedStackedInline, StackedInline):
    model = Answer
    extra = 3
    max_num = 3

class QuestionInline(nested_admin.NestedStackedInline, StackedInline):
    model = Question
    inlines = (AnswerInline, )
    extra = 1
    max_num = 10

@admin.register(TestCategory)
class TestCategoryAdmin(ModelAdmin):
    pass

@admin.register(Test)
class TestModelAdmin(nested_admin.NestedModelAdmin, ModelAdmin):
    inlines = (QuestionInline, )
    readonly_fields = ('users', )

@admin.register(Question)
class QuestionModeAdmin(nested_admin.NestedModelAdmin, ModelAdmin):
    inlines = (AnswerInline, )

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False


