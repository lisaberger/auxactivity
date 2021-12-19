from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.conf import settings
from django.db.models.signals import post_save
from .models import UserProfile


# Create your views here.


def profile_view(request):
    current_user = request.user
    user_profile = UserProfile.objects.get(user_id=request.user.id)

    context = {
        'user': current_user,
        'profile': user_profile
    }

    return render(request, 'registration/profile.html', context)


def login_view(request):
    pass


def logout_view(request):
    pass


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')

    else:
        form = UserCreationForm()
        return render(request, 'registration/register.html', dict(form=form))


def post_save_receiver(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfile(user=instance)
        user_profile.save()


post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)
