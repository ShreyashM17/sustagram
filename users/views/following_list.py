from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from users.models import User

@login_required
def following_list_view(request, username):
  profile_user = get_object_or_404(User, username=username)
  following_users = User.objects.filter(followers__user=profile_user)

  return render(request, 'users/following_list.html', {
    'profile_user': profile_user,
    'following_users': following_users
  })
