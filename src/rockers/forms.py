from django import forms
from .models import *


class AddPostForm(forms.Form):
    name = forms.CharField(max_length=255, label='Name of Rocker')
    slug = forms.SlugField(max_length=255, label='URL')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Content')
    is_published = forms.BooleanField(label='Needed to be published?', initial=True)
    role = forms.ModelChoiceField(queryset=Role.objects.all(), label='Role', empty_label='Role is not choosen')
