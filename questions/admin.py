from django.contrib import admin

from questions.models import Question


class QuestionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Question, QuestionAdmin)
