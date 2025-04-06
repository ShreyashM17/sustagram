from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from posts.models import Post
from users.models import Follow
from django.core.paginator import Paginator

@login_required
def feed_view(request):
  posts = Post.objects.select_related('user').prefetch_related('comments__user').order_by('-created_at')

  # Get list of usernames the current user follows
  following_user_ids = set(
    Follow.objects.filter(user=request.user).values_list('target_id', flat=True)
  )
  tag = request.GET.get('tag')
  if tag:
    posts = posts.filter(tag=tag)

  paginator = Paginator(posts, 5)  # 5 posts per page
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

  return render(request, 'posts/feed.html', {
    'page_obj': page_obj,
    'following_user_ids': following_user_ids,
  })
