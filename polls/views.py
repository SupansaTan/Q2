from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import datetime

from .models import Choice, Question, Vote

tz = timezone.get_default_timezone()

# Create your views here.
def index(request):
    sort = request.GET.get('sort','default')
    reverse = bool(int(request.GET.get('reverse',0))) # 0: reverse = true, 1: reverse = false

    if sort == 'default': # when not sort
        question_list = Question.objects.order_by('-pub_date')[:5]
        return render(request, 'polls/index.html', {
                'latest_question_list': question_list,
        })

    elif sort == 'votes': # clicked dropdown to sort by votes
        question_list = []
        question_sorted = []
        questions = Question.objects.all()

        # sort questions by sum votes
        for question in questions:
            question_obj = {'question':question, 'votes':question.get_sum_score()} # get sum votes of each question
            question_list.append(question_obj)

        question_list = sorted(question_list, key=lambda question: question['votes'], reverse=reverse)

        for question_obj in question_list:
            question_sorted.append(question_obj['question'])

        return render(request, 'polls/index.html', {
            'latest_question_list': question_sorted
        })

    elif sort == 'vote_time': # clicked dropdown to sort by vote time
        question_list = []
        question_sorted = []
        questions = Question.objects.all()

        for question in questions:
            try:
                question_obj = {'question':question, 'votetime':question.get_latest_vote_time()} # get last vote time of each question
            except ObjectDoesNotExist:
                question_obj = {'question':question, 'votetime':datetime.datetime(1970, 1, 1).astimezone(tz)}

            question_list.append(question_obj)

        
        question_list = sorted(question_list, key=lambda question: question['votetime'], reverse=reverse)
        print(question_list )
        for question_obj in question_list:
            question_sorted.append(question_obj['question'])

        return render(request, 'polls/index.html', {
            'latest_question_list': question_sorted
        })

def detail(request, question_id):
    # get detail
    question = Question.objects.get(pk=question_id)

    return render(request, 'polls/detail.html', {
            'question': question
        })