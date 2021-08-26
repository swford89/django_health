from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from polls.models import Question, Choice, Mood

# Create your views here.
def index(request):
    latest_questions_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_questions_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'polls/detail.html', context)

def submit(request, question_id):
    mood_level = int(request.POST['mood_level'])
    question = get_object_or_404(Question, pk=question_id)
    user_mood = Mood(mood_level=mood_level, user_feedback=request.POST['user_feedback'], mood_date=timezone.now())
    user_mood.save()
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
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    user_mood = Mood.objects.latest('mood_date')
    print(user_mood.mood_level)
    context = {
        'question': question,
        'user_mood': user_mood,
        }
    return render(request, 'polls/results.html', context)