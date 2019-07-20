from django import forms
from . import models
# from .models import Post, Comment

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title','body','slug']

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ('author', 'text',)