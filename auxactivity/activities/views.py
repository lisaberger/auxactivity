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
    all_categories = models.Category.objects.all()
    category_selected = request.GET.get('category_selected')
    name_search_query = request.GET.get('name_search')

    if category_selected != '' and category_selected is not None:
        all_activities = all_activities.filter(categories__name=category_selected)

    elif name_search_query != '' and name_search_query is not None:
        all_activities = all_activities.filter(name__icontains=name_search_query)

    context = {
        'activities': all_activities,
        'categories': all_categories
    }

    return render(request, 'activities.html', context)


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



def filter_form(request):
    all_categories = models.Category.objects.all()

    category_id = request.GET.get('category')  # nur Text oder None

    if category_id:
        activities = models.Activity.objects.filter(categories=int(category_id))
    else:
        activities = []

    return render(request, 'choose.html', dict(
        categories=all_categories,
        activities=activities,
    ))




