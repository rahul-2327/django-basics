from django.shortcuts import render
from django.http import HttpResponse
from .models import ChaiVarity
from django.shortcuts import get_object_or_404

# Create your views here.


def home(request):

    # return HttpResponse('<h1>You are at the home page</h1>')
    return render(request, 'website/index1.html')


def about(req):
    return render(req, 'website/about.html')


def contact(req):
    return render(req, "website/contact.html")


def all_chai(req):
    chais = ChaiVarity.objects.all()
    return render(req, 'chai/all_chai.html', {'chais': chais})


def chai_details(req, chai_id):
    chai = get_object_or_404(ChaiVarity, pk=chai_id)
    return render(req, 'chai/chai_details.html', {'chai':chai})
