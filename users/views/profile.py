from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from users.models import User, Follow
from posts.models import Post

@login_required
def profile_view(request, username):
  profile_user = get_object_or_404(User, username=username)
  posts = Post.objects.filter(user=profile_user).order_by('-created_at')

  is_following = False
  if request.user != profile_user:
    is_following = Follow.objects.filter(user=request.user, target=profile_user).exists()

  return render(request, 'users/profile.html', {
    'profile_user': profile_user,
    'posts': posts,
    'is_following': is_following,
  })
