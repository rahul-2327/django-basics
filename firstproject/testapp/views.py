from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def say_hello(request):
    # what we can do here?
    # anything we want
    # like pull data from database
    # transform data
    # send email
    # returning a instance of HttpResponse class
    return HttpResponse('hello world')
    # now we need to map this view to a url so that when we get request at that url this function will be called.


def greeting(request):
    s = "hello and welcome to first view"
    return HttpResponse(s)


def about(request):
    str = "rahul"
    context = {
        "str": str
    }
    template = loader.get_template('about.html')
    res = template.render(context, request)
    return HttpResponse(res)


def contact(request):
    s = "<h1>Contact us at 3298523539</h1>"
    return HttpResponse(s)
