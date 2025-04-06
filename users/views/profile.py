from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from users.models import User, Follow
from posts.models import Post, Comment

@login_required
def profile_view(request, username):
  profile_user = get_object_or_404(User, username=username)
  posts = Post.objects.select_related('user').prefetch_related('comments__user').order_by('-created_at')
  comments = Comment.objects.filter(user=profile_user).select_related('post').order_by('-created_at')

  is_following = False
  if request.user != profile_user:
    is_following = Follow.objects.filter(user=request.user, target=profile_user).exists()

  return render(request, 'users/profile.html', {
    'profile_user': profile_user,
    'posts': posts,
    'comments': comments,
    'is_following': is_following,
  })
