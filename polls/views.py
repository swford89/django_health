from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from polls.models import Post, Question, Choice, User

# Create your views here.
def index(request):
    latest_posts_list = Post.objects.order_by('-pub_date')[:5]
    context = {
        'latest_posts_list': latest_posts_list
        }
    return render(request, 'polls/index.html', context)

def detail(request, post_slug):
    post = get_object_or_404(Post, post_slug=post_slug)
    question_list = Question.objects.all()
    for question in question_list:
        if post == question.post:
            question = question
    context = {
        'post': post,
        'question': question
        }
    return render(request, 'polls/detail.html', context)

def submit(request, post_slug):
    mood_level = int(request.POST['mood_level'])
    user_info = User(like_rating=mood_level, user_feedback=request.POST['user_feedback'], feedback_date=timezone.now())
    user_info.save()
    post = get_object_or_404(Post, post_slug=post_slug)
    question_list = Question.objects.all()
    for question in question_list:
        if post == question.post:
            question = question
    try:
        # get submitted data from DB
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # redisplay detail page for invalid submissions
        context = {
            'question': question,
            'error_message': "You didn't select a choice."
            }
        return render(request, 'polls/detail.html', context)
    else:
        # increment vote tally for selected choice and save
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(post.post_slug,)))

def results(request, post_slug):
    post = get_object_or_404(Post, post_slug=post_slug)
    question_list = Question.objects.all()
    for question in question_list:
        if post == question.post:
            question = question
    user_info = User.objects.latest('feedback_date')
    context = {
        'post': post,
        'question': question,
        'user_info': user_info,
        }
    return render(request, 'polls/results.html', context)