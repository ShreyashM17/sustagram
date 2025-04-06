from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Follow

@admin.register(User)
class UserAdmin(BaseUserAdmin):
  list_display = ('username', 'email', 'is_ngo', 'is_company', 'green_score', 'last_active')
  fieldsets = BaseUserAdmin.fieldsets + (
    ('Sustagram Info', {'fields': ('is_ngo', 'is_company', 'green_score')}),
  )

admin.site.register(Follow)