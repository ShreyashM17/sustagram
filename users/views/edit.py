from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.forms import EditProfileForm

@login_required
def edit_profile(request):
  if request.method == 'POST':
    form = EditProfileForm(request.POST, instance=request.user)
    if form.is_valid():
      form.save()
      return redirect('profile', username=request.user.username)
  else:
    form = EditProfileForm(instance=request.user)
  return render(request, 'users/edit_profile.html', {'form': form})
