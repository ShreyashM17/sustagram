from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from posts.models import Post, Comment
from posts.forms import CommentForm

@login_required
def post_detail_view(request, post_id):
  post = get_object_or_404(Post.objects.select_related('user'), id=post_id)
  comments = post.comments.select_related('user').order_by('created_at')

  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
      comment = form.save(commit=False)
      comment.post = post
      comment.user = request.user
      comment.save()
      return redirect('post_detail', post_id=post.id)
  else:
    form = CommentForm()

  return render(request, 'posts/detail.html', {
    'post': post,
    'comments': comments,
    'form': form
  })
