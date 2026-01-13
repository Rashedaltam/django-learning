from django.contrib import admin
from .models import Question, Choice
from django.utils import timezone

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)