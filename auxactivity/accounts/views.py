from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.shortcuts import render, redirect
from django.conf import settings
from django.db.models.signals import post_save
from .models import Profile
from activities import models
from django.contrib.auth.decorators import login_required


# Create your views here.


class ProfileForm(forms.ModelForm):
    """Klasse zur Formularerstellung"""
    class Meta:
        model = Profile
        fields = ('avatar',)


class SignUpForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')


@login_required()
def profile_view(request):
    current_user = request.user
    user_profile = Profile.objects.get(user_id=current_user.id)
    created_activities = models.Activity.objects.filter(creator_id=current_user.id)
    joined_activities = models.Activity.objects.filter(participants=current_user)

    context = {
        'user': current_user,
        'profile': user_profile,
        'created_activities': created_activities,
        'joined_activities': joined_activities,
    }

    return render(request, 'registration/profile.html', context)


@login_required()
def edit_profile_view(request):
    current_user = request.user
    user_profile = Profile.objects.get(user_id=current_user.id)

    context = {
        'user': current_user,
        'profile': user_profile,
    }

    return render(request, 'registration/editprofile.html', context)


def login_view(request):
    pass


def logout_view(request):
    pass


def register_view(request):
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     profile_form = ProfileForm(request.POST)
    #
    #     if form.is_valid():
    #         form.save()
    #         return redirect('login_url')
    #
    # else:
    #     form = UserCreationForm()
    #     profile_form = ProfileForm()
    #
    # return render(request, 'registration/register.html', dict(form=form, profile_form=profile_form))

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.avatar = form.cleaned_data.get('avatar')
            profile_form.save()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('login_url')
    else:
        form = SignUpForm()
        profile_form = ProfileForm()
    return render(request, 'registration/register.html', {'form': form, 'profile_form': profile_form})


def post_save_receiver(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()


post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)