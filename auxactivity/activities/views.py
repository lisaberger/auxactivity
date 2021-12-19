from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import models

# Create your views here.


class ActivityForm(forms.ModelForm):
    """Klasse zur Formularerstellung"""
    class Meta:
        model = models.Activity
        exclude = ['creator', 'participants']


def activity_overview(request):
    all_activities = models.Activity.objects.all()
    all_categories = models.Category.objects.all()
    category_selected = request.GET.get('category_selected')
    # categories_selected = request.GET.getlist('category_selected')
    name_search_query = request.GET.get('name_search')

    if category_selected != '' and category_selected is not None:
        all_activities = all_activities.filter(categories__name=category_selected)
        # all_activities = all_activities.filter(categories__name__in=categories_selected).distinct()

    elif name_search_query != '' and name_search_query is not None:
        all_activities = all_activities.filter(name__icontains=name_search_query)

    context = {
        'activities': all_activities,
        'categories': all_categories
    }

    # An Aktivität teilnehmen
    # activity_id = request.GET['activity_to_participate']
    # activity = models.Activity.objects.all().get(id=activity_id)
    # print(activity_id)
    # current_user = request.user
    # activity.participants.add(current_user)
    # activity.save()

    return render(request, 'activities.html', context)


def add_activity_view(request):
    # werden Formulardaten geschickt?
    if request.method == "POST":
        form = ActivityForm(request.POST, request.FILES)
        form.instance.creator = request.user
        if form.is_valid():  # Formular überprüfen
            form.save()
            return HttpResponseRedirect('/act/activities')  # Umleitung
    else:
        form = ActivityForm()  # leeres Formular
    return render(request, 'newactivity.html', dict(form=form))


def activity_detail_view(request, activity_id):
    # activity_id = request.GET['id']
    activity = models.Activity.objects.all().get(id=activity_id)
    return render(request, 'activity.html', dict(activity=activity))


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




