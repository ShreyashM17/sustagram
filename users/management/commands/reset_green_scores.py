from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from users.models import User

class Command(BaseCommand):
  help = 'Reset green scores for users inactive for 7+ days'

  def handle(self, *args, **kwargs):
    threshold = timezone.now() - timedelta(days=7)
    inactive_users = User.objects.filter(
      last_post_at__lt=threshold,
      green_score__gt=0
    )

    for user in inactive_users:
      self.stdout.write(f"Resetting score for {user.username}")
      user.green_score = 0
      user.save(update_fields=["green_score"])

    self.stdout.write(self.style.SUCCESS(
      f"Reset green score for {inactive_users.count()} inactive users"
    ))
