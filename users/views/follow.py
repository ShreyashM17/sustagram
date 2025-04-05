from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from users.models import User, Follow

@login_required
def toggle_follow(request, username):
  target_user = get_object_or_404(User, username=username)

  if target_user == request.user:
    # Prevent self-following
    return redirect('profile', username=username)

  existing = Follow.objects.filter(user=request.user, target=target_user)
  if existing.exists():
    existing.delete()
  else:
    Follow.objects.create(user=request.user, target=target_user)

  return redirect('profile', username=username)
