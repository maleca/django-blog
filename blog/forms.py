from django import forms
from .models import Post
from tinymce.models import HTMLField
from tinymce.widgets import TinyMCE


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    subtitle=forms.CharField(max_length=100)
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    image = forms.ImageField()

    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'content', 'image')


