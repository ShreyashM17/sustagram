from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from users.models import User

@login_required
def followers_list_view(request, username):
  profile_user = get_object_or_404(User, username=username)
  followers = User.objects.filter(following__target=profile_user)

  return render(request, 'users/followers_list.html', {
    'profile_user': profile_user,
    'followers': followers
  })