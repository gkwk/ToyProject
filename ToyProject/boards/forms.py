from django import forms
from .models import Comment, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("user_id" ,"user_id_char", "title" ,"content", "updated_bool","visible_bool")
        # fields = ("uploader_id", "title" ,"content")



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("post_id", "user_id" ,"user_id_char", "comment_content", "updated_bool","visible_bool")
        # fields = ("post_id", "user_id" ,"user_id_char", "comment_content")