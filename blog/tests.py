import datetime
from django.test import TestCase
from django.utils import timezone
from blog.models import Post, Question

# Create your tests here.
class PostModelTests(TestCase):

    def test_post_published_recently_with_future_post(self):
        """
        post_published_recently() returns False for posts whose pub_date is in the future
        """
        future_time = timezone.now() + datetime.timedelta(days=30)
        future_post = Post(pub_date=future_time)
        self.assertIs(future_post.post_published_recently(), False)

    def test_post_published_recently_with_past_post(self):
        """
        post_published_recently() returns False for posts whose pub_date is more than 1 day in the past
        """
        past_time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        past_post = Post(pub_date=past_time)
        self.assertIs(past_post.post_published_recently(), False)

    def test_post_published_recently_with_recent_post(self):
        """
        post_published_recently() returns True for posts whose pub_date is within the last 24 hours
        """
        recent_time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_post = Post(pub_date=recent_time)
        self.assertIs(recent_post.post_published_recently(), True)

def create_post(title, days):
    """
    create a post with a `title` and a `pub_date` with a given number of days offset
    - = past
    + = future
    """
    return 