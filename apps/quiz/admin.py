from django.contrib import admin
from .models import TestCategory, Test, Question, Answer

# Register your models here.

class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 4


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1
    inlines = (AnswerInline, )


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = (AnswerInline, )

@admin.register(TestCategory)
class TestCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    inlines = (QuestionInline, AnswerInline)