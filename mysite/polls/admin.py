from django.contrib import admin

# Register your models here.
from .models import Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdamin):

    list_display = ('question_text','pub_date','was_published_recently')

    fieldsets = [
                   (None,               {'fields':['question_text']}),
                   ('Date information', {'fields':['pub_date']}),
                ]   

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)

