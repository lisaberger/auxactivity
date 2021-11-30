from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import models

# Create your views here.


class ActivityForm(forms.ModelForm):
    """Klasse zur Formularerstellung"""
    class Meta:
        model = models.Activity
        exclude = []


def activity_overview(request):
    all_activities = models.Activity.objects.all()
    return render(request, 'activities.html', dict(activities=all_activities))


def add_activity_view(request):
    # werden Formulardaten geschickt?
    if request.method == "POST":
        form = ActivityForm(request.POST, request.FILES)
        if form.is_valid():  # Formular überprüfen
            form.save()
            return HttpResponseRedirect('/activities')  # Umleitung
    else:
        form = ActivityForm()  # leeres Formular
    return render(request, 'newactivity.html', dict(form=form))
