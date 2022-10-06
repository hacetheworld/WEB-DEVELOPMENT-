from multiprocessing import context
import re
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from playground.models import Contact
# Create your views here.


def say_hello(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "services.html")


def contact(request):
    if request.method == "POST":
        email = request.POST.get('email')
        message = request.POST.get('desc')
        contact = Contact(email=email, message=message,
                          date=datetime.today())
        contact.save()
        messages.success(request, 'Message Has been Sent !')

    return render(request, "contact.html")
