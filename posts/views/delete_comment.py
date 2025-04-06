from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from posts.models import Comment
from django.contrib import messages

@login_required
def delete_comment(request, comment_id):
  comment = get_object_or_404(Comment, id=comment_id)

  if comment.user != request.user:
    messages.error(request, "You can't delete this comment.")
    return redirect('post_detail', post_id=comment.post.id)

  comment.delete()
  messages.success(request, "Comment deleted.")
  return redirect('post_detail', post_id=comment.post.id)
