from django.urls import path
from posts.views import upload, feed, following, delete, detail, delete_comment

urlpatterns = [
  path('upload/', upload.upload_post, name='upload_post'),
  path('feed/', feed.feed_view, name='feed'),
  path('following/', following.personal_feed_view, name='personal_feed'),
  path('<int:post_id>/delete/', delete.delete_post, name='delete_post'),
  path('<int:post_id>/', detail.post_detail_view, name='post_detail'),
  path('comment/<int:comment_id>/delete/', delete_comment.delete_comment, name='delete_comment'),
]