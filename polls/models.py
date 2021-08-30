import datetime
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from autoslug import AutoSlugField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    post = models.TextField()
    pub_date = models.DateTimeField('date_published')
    post_slug = AutoSlugField(populate_from='title', unique=True)

    def save(self, *args, **kwargs):
        """overwrites internal save() to automatically create a slug, if not provided"""
        if not self.post_slug:
            self.post_slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def post_published_recently(self):
        return datetime.timedelta(days=1) <= self.pub_date <= timezone.now()

class Question(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    pub_date = models.DateTimeField('date_published')
    question_slug = AutoSlugField(populate_from='title', unique=True)

    def save(self, *args, **kwargs):
        """overwrites internal save() to automatically create a slug, if not provided"""
        if not self.question_slug:
            self.question_slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return datetime.timedelta(days=1) <= self.pub_date <= timezone.now()

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=150)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class User(models.Model):
    like_rating = models.IntegerField(default=0)
    user_feedback = models.TextField()
    feedback_date = models.DateTimeField(auto_now_add=True)