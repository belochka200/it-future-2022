from django import forms
from .models import Post


class RegForm(forms.Form):
    username = forms.CharField(max_length=12)
    email = forms.EmailField()
    password = forms.CharField(max_length=128)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'category')