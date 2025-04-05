from django.contrib import admin
from .models import Post
from django.utils.html import format_html

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ('user', 'tag', 'created_at', 'thumbnail')

  def thumbnail(self, obj):
    if obj.image:
      return format_html('<img src="{}" width="80" style="border-radius: 4px;" />', obj.image.url)
    return "-"
  thumbnail.short_description = "Preview"

