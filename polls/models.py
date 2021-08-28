import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=150)
    post = models.TextField()
    pub_date = models.DateTimeField('date_published')

    def post_published_recently(self):
        return datetime.timedelta(days=1) <= self.pub_date <= timezone.now()

class Question(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=150)
    pub_date = models.DateTimeField('date_published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return datetime.timedelta(days=1) <= self.pub_date <= timezone.now()

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=150)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Mood(models.Model):
    mood_level = models.IntegerField(default=0)
    user_feedback = models.TextField()
    mood_date = models.DateTimeField(auto_now_add=True)