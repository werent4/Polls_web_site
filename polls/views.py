from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Question, Choice, Vote
from .utils import has_voted

# Create your views here.

@login_required
def index(request):
    order_by = request.GET.get('order_by', '-pub_date')
    latest_question_list = Question.objects.order_by(order_by)[:]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)
@login_required
def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    conext = {
        'question': question
    }
    return render(request, 'polls/detail.html', conext)

@login_required
def results(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    context = {
        'question' : question,
    }
    return render(request, 'polls/results.html', context)


@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question,
        'error_messege': 'You didnt select a choice.'
    }

    # Проверяем, что пользователь еще не голосовал в текущем опросе
    if Vote.objects.filter(user=request.user, question=question).exists():
        return render(request, 'polls/alrd_voted.html', {'question': question})

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()

        # Создаем запись о голосовании в таблице Vote
        vote = Vote(user=request.user, question=question, choice=selected_choice)
        vote.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
