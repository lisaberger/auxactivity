from django.shortcuts import render
from accounts.models import Profile

# Create your views here.


def startpage_view(request):
    current_user = request.user
    print(current_user)
    try:
        user_profile = Profile.objects.get(user_id=current_user.id)
    except Profile.DoesNotExist:
        user_profile = None

    context = {
            'profile': user_profile
        }

    return render(request, 'index.html', context)
