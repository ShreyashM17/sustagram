from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field in self.fields.values():
      field.widget.attrs.update({
        'class': (
          'mt-1 block w-full px-3 py-2 border border-gray-300 '
          'rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500'
        )
      })

class CustomUserCreationForm(UserCreationForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field in self.fields.values():
      field.widget.attrs.update({
        'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-green-500 focus:border-green-500'
      })

  USER_TYPE_CHOICES = [
    ('individual', 'Individual'),
    ('ngo', 'NGO'),
    ('company', 'Company'),
  ]

  user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, label="I am a", widget=forms.Select())

  class Meta:
    model = User
    fields = ('username', 'email', 'user_type', 'password1', 'password2')

  def save(self, commit=True):
    user = super().save(commit=False)
    user_type = self.cleaned_data['user_type']

        # Set role based flags
    if user_type == 'ngo':
      user.is_ngo = True
    elif user_type == 'company':
      user.is_company = True
    # Individual is default (neither flag)

    if commit:
      user.save()
      return user


class EditProfileForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['bio']

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field in self.fields.values():
      field.widget.attrs.update({
        'class': (
          'mt-1 block w-full px-3 py-2 border border-gray-300 '
          'rounded-md shadow-sm focus:ring-green-500 focus:border-green-500'
        )
      })