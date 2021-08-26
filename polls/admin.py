from polls.models import Question, Choice, Mood
from django.contrib import admin

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Mood)