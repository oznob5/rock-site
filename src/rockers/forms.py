from django import forms
from .models import *
from django.core.exceptions import ValidationError


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['role'].empty_label = "Role is not selected"

    def clean_name(self):
        name = self.cleaned_data['name']  # get data from form
        if len(name) > 50:
            raise ValidationError('Length of the name if more than 50 chars')
        return name

    class Meta:
        model = Post
        fields = ['name', 'slug', 'content', 'photo', 'is_published', 'role']
