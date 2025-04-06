from django.urls import path
from users.views import auth, home, leaderboard, profile, follow, edit, following_list, followers_list, dashboard

urlpatterns = [
  path('', home.home_view, name='home'),
  path('signup/', auth.signup_view, name='signup'),
  path('login/', auth.login_view, name='login'),
  path('logout/', auth.logout_view, name='logout'),
  path('leaderboard/', leaderboard.leaderboard_view, name='leaderboard'),
  path('profile/<str:username>/', profile.profile_view, name='profile'),
  path('profile/<str:username>/follow/', follow.toggle_follow, name='toggle_follow'),
  path('edit-profile/', edit.edit_profile, name='edit_profile'),
  path('profile/<str:username>/following/', following_list.following_list_view, name='following_list'),
  path('profile/<str:username>/followers/', followers_list.followers_list_view, name='followers_list'),
  path('dashboard/', dashboard.dashboard_view, name='dashboard'),
]