from django.contrib import admin
from .models import Question, Answer

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'nickname', 'created_at')
    search_fields = ('question', 'nickname__username')
    list_filter = ('created_at',)
    raw_id_fields = ('nickname',)

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer', 'nickname', 'question', 'created_at')
    search_fields = ('answer', 'nickname__username', 'question__question')
    list_filter = ('created_at',)
    raw_id_fields = ('nickname', 'question')

