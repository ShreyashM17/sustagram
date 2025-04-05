from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class User(AbstractUser):
  is_ngo = models.BooleanField(default=False)
  is_company = models.BooleanField(default=False)
  green_score = models.IntegerField(default=0)
  last_active = models.DateTimeField(auto_now=True)
  bio = models.TextField(blank=True, max_length=300)
  last_post_at = models.DateTimeField(null=True, blank=True)

  def reset_green_score(self):
    # TODO: implement weekly inactivity check
    pass


class Follow(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following')
  target = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followers')
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    unique_together = ('user', 'target')

  def __str__(self):
    return f"{self.user.username} follows {self.target.username}"