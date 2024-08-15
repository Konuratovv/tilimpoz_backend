from django.contrib import admin
from .models import Question, Answer


class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 1

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'nickname', 'created_at')
    search_fields = ('question', 'nickname__username')
    list_filter = ('created_at',)
    raw_id_fields = ('nickname',)
    inlines = (AnswerInline, )



