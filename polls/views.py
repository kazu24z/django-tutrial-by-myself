from django import urls
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.template import loader

from polls.models import Question, Choice

# Create your views here.


# render()ショートカット
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))


# 詳細
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {"question": question}
    return render(request, "polls/detail.html", context)


def vote(request, question_id):
    # questionと、それに紐づくchoiceリストを取得
    question = get_object_or_404(Question, pk=question_id)

    # Choiceのvotesを更新する
    voted_choice = question.choice_set.get(pk=request.POST.get('choice'))
    voted_choice.votes += 1
    voted_choice.save()

    # templateにデータを渡して、resultに処理を渡す
    return redirect(urls.reverse('polls:results', args=[question_id]))


def results(request, question_id):
    question = Question.objects.get(pk=question_id)
    choices = question.choice_set.all()
    context = {
        "question": question,
        "choices": choices
    }
    return render(request, "polls/results.html", context)
