from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from polls.models import Question

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
    pass


def result(request, question_id):
    pass
