from django.shortcuts import render
from django.http import HttpResponse
from .forms import *

def home(request):
    form = SubscriberForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        new_form = form.save()

    return render(request, 'landing/landing.html', locals())



