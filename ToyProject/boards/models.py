from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    # uploader_id = models.CharField(db_column='uploader_id', max_length=150, blank=True, null=True)
    user_id = models.ForeignKey(User, related_name="post",db_column="user_id",on_delete=models.CASCADE,blank=False,null=False)
    user_id_char = models.CharField(max_length=150,blank=False,null=False)
    title = models.CharField(db_column='title', max_length=50, blank=False, null=False)
    content = models.TextField(db_column='content', default="",blank=False,null=False)
    created_date = models.DateTimeField(db_column='created_date', auto_now_add=True)
    updated_date = models.DateTimeField(db_column='updated_date', auto_now=True)
    updated_bool = models.BooleanField(db_column='updated_bool', default=False,blank=False,null=False)
    visible_bool = models.BooleanField(db_column='visible_bool', default=True,blank=False,null=False)
    # date_text = models.TextField(db_column='date_text', default="")
    

class Comment(models.Model):
    id = models.BigAutoField(primary_key=True) 
    post_id = models.ForeignKey(Post, related_name="comment",db_column="post_id",on_delete=models.CASCADE,blank=False,null=False)
    user_id = models.ForeignKey(User, related_name="comment",db_column="user_id",on_delete=models.CASCADE,blank=False,null=False)
    # post_id = models.ForeignKey(Post, related_name="comment",db_column="post_id",blank=False,null=False)
    # user_id = models.ForeignKey(User, related_name="comment",db_column="user_id",blank=False,null=False)
    user_id_char = models.CharField(max_length=150,blank=False,null=False)
    comment_content = models.CharField(max_length=300,blank=False,null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    updated_bool = models.BooleanField(db_column='updated_bool', default=False,blank=False,null=False)
    visible_bool = models.BooleanField(db_column='visible_bool', default=True,blank=False,null=False)

