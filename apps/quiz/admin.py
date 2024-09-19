import nested_admin

from django.contrib import admin
from django.http.request import HttpRequest

from .models import TestCategory, Test, Question, Answer

# Register your models here.

class AnswerInline(nested_admin.NestedStackedInline):
    model = Answer
    extra = 4
    max_num = 4

class QuestionInline(nested_admin.NestedStackedInline):
    model = Question
    inlines = (AnswerInline, )
    extra = 1
    max_num = 10

@admin.register(TestCategory)
class TestCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Test)
class TestModelAdmin(nested_admin.NestedModelAdmin):
    inlines = (QuestionInline, )
    readonly_fields = ('users', )

@admin.register(Question)
class QuestionModeAdmin(nested_admin.NestedModelAdmin):
    inlines = (AnswerInline, )

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False


