from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from posts.forms import PostForm
from django.contrib import messages
from django.utils import timezone

GREEN_SCORE_PER_POST = 10

@login_required
def upload_post(request):
  if request.method == 'POST':
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
      post = form.save(commit=False)
      post.user = request.user
      post.save()

      post.user.green_score += GREEN_SCORE_PER_POST
      post.user.last_post_at = timezone.now()
      post.user.save(update_fields=["green_score", "last_post_at"])

      # ✅ Boost green score
      request.user.green_score += GREEN_SCORE_PER_POST
      request.user.save(update_fields=["green_score"])

      messages.success(request, f"Post shared! 🌱 Your green score increased by {GREEN_SCORE_PER_POST}!")
      return redirect('feed')
  else:
    form = PostForm()
  return render(request, 'posts/upload.html', {'form': form})
