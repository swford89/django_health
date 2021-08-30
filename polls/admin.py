from polls.models import Post, Question, Choice, User
from django.contrib import admin

# Register your models here.
admin.site.register(Post)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(User)