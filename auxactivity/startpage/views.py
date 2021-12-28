from django.shortcuts import render
from accounts.models import UserProfile

# Create your views here.


def startpage_view(request):
    current_user = request.user
    # print(current_user)
    # if current_user != "AnonymousUser":
    #     user_profile = UserProfile.objects.get(user_id=current_user.id)
    #
    context = {
 # 'profile': user_profile
    }

    return render(request, 'index.html', context)
