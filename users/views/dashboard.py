from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from posts.models import Post
from django.utils import timezone
from datetime import timedelta

@login_required
def dashboard_view(request):
  user = request.user

  # Weekly post counts (last 7 days)
  today = timezone.now().date()
  daily_counts = []
  labels = []

  for i in range(6, -1, -1):
    day = today - timedelta(days=i)
    count = Post.objects.filter(user=user, created_at__date=day).count()
    daily_counts.append(count)
    labels.append(day.strftime('%a'))  # Mon, Tue...

  progress = get_badge_progress(request.user.green_score)

  return render(request, 'users/dashboard.html', {
    'user': request.user,
    'labels': labels,
    'daily_counts': daily_counts,
    'progress': progress,
  })


def get_badge_progress(score):
  thresholds = [0, 1, 50, 150, 300]
  labels = ["🐣 Just Starting", "🍃 Eco Explorer", "🌿 Green Advocate", "🌳 Hero", "🦸‍♂️ Legend"]

  for i in range(len(thresholds) - 1):
    if thresholds[i] <= score < thresholds[i + 1]:
      return {
        "current": labels[i],
        "next": labels[i + 1],
        "from_score": thresholds[i],
        "to_score": thresholds[i + 1],
        "percent": round((score - thresholds[i]) / (thresholds[i + 1] - thresholds[i]) * 100)
      }

  # If maxed out
  return {
    "current": labels[-1],
    "next": None,
    "from_score": thresholds[-1],
    "to_score": thresholds[-1],
    "percent": 100
  }