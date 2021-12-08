from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import models

# Create your views here.
def startpage_overview(request):
    return render(request, 'startpage.html')

