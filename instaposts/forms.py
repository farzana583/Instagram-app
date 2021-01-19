from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['content']


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user','likes']