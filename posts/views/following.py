from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from posts.models import Post
from users.models import Follow
from django.core.paginator import Paginator

@login_required
def personal_feed_view(request):
  followed_users = Follow.objects.filter(user=request.user).values_list('target_id', flat=True)
  posts = Post.objects.filter(user_id__in=followed_users).select_related('user').order_by('-created_at')

  following_user_ids = set(followed_users)
  paginator = Paginator(posts, 5)  # 5 posts per page
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

  return render(request, 'posts/following_feed.html', {
    'page_obj': page_obj,
    'following_user_ids': following_user_ids,
  })