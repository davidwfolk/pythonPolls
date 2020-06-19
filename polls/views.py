from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Question


# Create your views here.
  #NOTE SIMPLE http response
# def index(request, question_id):
#     return HttpResponse("You're looking at the results of %s." % question_id)

def index(request):
    #NOTE V1
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

  # NOTE V2 using index.html in templates
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))

    #NOTE v3 with render vs HttpResponse
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question': question})
    
    # NOTE SAME AS ABOVE
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    return HttpResponse("You're looking at the results of %s." % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
