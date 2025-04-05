from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from users.models import User

@login_required
def leaderboard_view(request):
  top_users = User.objects.order_by('-green_score')[:10]
  return render(request, 'users/leaderboard.html', {'top_users': top_users})
