from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):

    # return HttpResponse('<h1>You are at the home page</h1>')
    return render(request, 'website/index.html')


def about(req):
    return render(req, 'website/about.html')


def contact(req):
    return render(req, "website/contact.html")
