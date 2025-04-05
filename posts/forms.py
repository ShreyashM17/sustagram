from django import forms
from .models import Post

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['image', 'tag', 'caption']

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field in self.fields.values():
      field.widget.attrs.update({
        'class': (
          'mt-1 block w-full px-3 py-2 border border-gray-300 '
          'rounded-md shadow-sm focus:ring-green-500 focus:border-green-500'
        )
      })
