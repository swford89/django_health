from blog.models import Post, Question, Choice, User
from django.contrib import admin

# Register your models here.

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {"fields": ["title"]}),
        ("Date Information",    {"fields": ['pub_date']}),
    ]

    inlines = [QuestionInline]
    list_display = ("title", "pub_date", "post_published_recently")

admin.site.register(Post, PostAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ("title", "pub_date")

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(User)