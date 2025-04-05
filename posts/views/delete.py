from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from posts.models import Post
from django.contrib import messages

@login_required
def delete_post(request, post_id):
  post = get_object_or_404(Post, id=post_id)

  if post.user != request.user:
    messages.error(request, "You are not allowed to delete this post.")
    return redirect('feed')

  post.delete()
  messages.success(request, "Post deleted successfully.")
  return redirect('profile', username=request.user.username)
