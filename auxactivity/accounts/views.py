from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.


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

