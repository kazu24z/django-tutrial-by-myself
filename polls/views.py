from typing import Any
from django import urls
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic

from polls.models import Question, Choice


# Create your views here.
class IndexView(generic.ListView):
    # model = Question
    context_object_name = 'latest_question_list'
    template_name = 'polls/index.html'

    def get_queryset(self) -> QuerySet[Any]:
        return Question.objects.order_by("-pub_date")[:5]


# 詳細
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


def vote(request, question_id):
    # questionと、それに紐づくchoiceリストを取得
    question = get_object_or_404(Question, pk=question_id)

    # Choiceのvotesを更新する
    voted_choice = question.choice_set.get(pk=request.POST.get('choice'))
    voted_choice.votes += 1
    voted_choice.save()

    # templateにデータを渡して、resultに処理を渡す
    return redirect(urls.reverse('polls:results', args=[question_id]))


class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
