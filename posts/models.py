from django.db import models
from users.models import User

class Post(models.Model):
  TAG_CHOICES = [
    ('recycle', 'Recycling'),
    ('planting', 'Planting Trees'),
    ('cleanup', 'Beach Cleanup'),
    ('awareness', 'Awareness Campaign'),
    ('other', 'Other'),
  ]

  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
  image = models.ImageField(upload_to='posts/')
  caption = models.TextField(blank=True)
  tag = models.CharField(max_length=50, choices=TAG_CHOICES)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f'{self.user.username} - {self.tag}'

