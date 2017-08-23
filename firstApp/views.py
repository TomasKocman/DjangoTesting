from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Question


def detail(request, questionID):
    question = get_object_or_404(Question, pk=questionID)

    return render(request, 'firstApp/detail.html', {'question': question})


def index(request):
    latestQuestionList = Question.objects.order_by('publicationDate')[:5]
    context = {
        'latestQuestionList': latestQuestionList
    }

    return render(request, 'firstApp/index.html', context)


def results(request, questionID):
    return HttpResponse('You are looking at the results of question {}.'.format(questionID))


def vote(request, questionID):
    return HttpResponse('You are voting on question {}.'.format(questionID))
