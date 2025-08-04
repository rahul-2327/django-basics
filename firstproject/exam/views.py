from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def testpaper(request):
    question = "Who Developed Python?"
    name1 = "rahul"
    name2 = "amit"
    name3 = "prabhat"
    name4 = "bauaa"
    context = {
        'que': question,
        'options' : [name1,name2,name3,name4]
    }
    template = loader.get_template('testpaper.html')
    res = template.render(context, request)
    return HttpResponse(res)


def result(request):
    s = "<p>You have failed</p>"
    return HttpResponse(s)
