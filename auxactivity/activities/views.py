from datetime import date

from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import models
from accounts.models import Profile

# Create your views here.


class ActivityForm(forms.ModelForm):
    """Klasse zur Formularerstellung"""
    class Meta:
        model = models.Activity
        exclude = ['creator', 'participants']


@login_required()
def activity_overview(request):
    # Logged in user profile picture
    current_user = request.user
    user_profile = Profile.objects.get(user_id=current_user.id)

    # Filters
    all_activities = models.Activity.objects.all()
    all_categories = models.Category.objects.all()

    categories_selected_query = request.GET.getlist('categories_selected')
    name_search_query = request.GET.get('name_search')
    date_query = request.GET.get('date')

    all_activities = all_activities.filter(Q(date__isnull=True) | Q(date__gte=date.today()))

    if categories_selected_query != [''] and categories_selected_query is not None:
        for category in categories_selected_query:
            all_activities = all_activities.filter(categories__name=category)

    if name_search_query != '' and name_search_query is not None:
        all_activities = all_activities.filter(name__icontains=name_search_query)

    if date_query != '' and date_query is not None:
        all_activities = all_activities.filter(
            Q(date=date_query) |
            Q(date__isnull=True)
        )

    context = {
        'activities': all_activities,
        'categories': all_categories,
        'profile': user_profile
    }

    # An Aktivität teilnehmen
    if request.POST:
        activity_id = request.POST['activity_to_participate']
        activity = models.Activity.objects.all().get(id=activity_id)
        current_user = request.user
        activity.participants.add(current_user)
        activity.save()

    return render(request, 'activity_overview.html', context)


@login_required()
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


@login_required()
def activity_detail_view(request, activity_id):
    activity = models.Activity.objects.all().get(id=activity_id)

    # Logged in user Profile Picture
    current_user = request.user
    user_profile = Profile.objects.get(user_id=current_user.id)

    # Creator Profile Picture
    creatorofActivity = activity.creator
    creator_profile = Profile.objects.get(user_id=creatorofActivity.id)

    # An Aktivität teilnehmen
    if request.POST:
        activity_id = request.POST.get('activity_to_participate', False)
        if activity_id:
            activity = models.Activity.objects.all().get(id=activity_id)
            #print(activity_id)
            current_user = request.user
            activity.participants.add(current_user)
            activity.save()

    # Aktivität absagen
    if request.POST:
        activity_id = request.POST.get('activity_to_cancel_participation', False)
        if activity_id:
            activity = models.Activity.objects.all().get(id=activity_id)
            print(activity_id)
            current_user = request.user
            activity.participants.remove(current_user)
            activity.save()

    return render(request, 'activity_detail.html',
                  dict(activity=activity,
                       user_profile=user_profile,
                       creator_profile=creator_profile)
                  )


def filter_form(request):
    all_categories = models.Category.objects.all()

    # Logged in user Profile Picture
    current_user = request.user
    user_profile = Profile.objects.get(user_id=current_user.id)

    category_id = request.GET.get('category')  # nur Text oder None

    if category_id:
        activities = models.Activity.objects.filter(categories=int(category_id))
    else:
        activities = []

    return render(request, 'choose.html', dict(
        categories=all_categories,
        activities=activities,
        userprofile=user_profile
    ))




