from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        #Blogger should only be able to modify title and body of the post
        fields = ('title', 'text',)
