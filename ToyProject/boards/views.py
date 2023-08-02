from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
import datetime

from boards.models import Post,Comment
from boards.forms import CommentForm,PostForm

# Create your views here.

def boards_index(request):
    Post_list = Post.objects.all()    
    context = {"Post_len" : len(Post_list), "Post_list" : Post_list}
    
    return render(request, 'boards/index.html', context=context)

def boards_posting(request):
    if request.user.is_superuser:
        if request.method == "POST":
            new_post = PostForm({
                "user_id" : request.user.id,
                "user_id_char" : request.user.username,
                "title" : request.POST.get("title"),
                "content" : request.POST.get("content"),
                "updated_bool" : False,
                "visible_bool" : True,
            })
                        
            if new_post.is_valid():
                new_post.save()
                return redirect('boards:index')
        
        return render(request, 'boards/posting.html')
    else:
        return redirect('/')

def boards_post_detail(request,pk):
    try:
        post = get_object_or_404(Post, pk=pk)
    except:
        return redirect("/")
    
    post_comment_list = Comment.objects.filter(post_id=pk).values("id","post_id","user_id","user_id_char","comment_content","created_date","updated_date","updated_bool","visible_bool") #쿼리셋을 얻는다.
    post_comment_list = list(post_comment_list) #쿼리셋을 리스트화한다.
        
    if request.user.is_authenticated:
        if request.method == "POST":
            new_CommentForm = CommentForm({"post_id" : pk,
                                           "user_id" : request.user.id,
                                           "user_id_char" : request.user.username,
                                           "comment_content" : request.POST.get("comment_content"),
                                           "updated_bool" : False,
                                           "visible_bool" : True,
                                           })

            if new_CommentForm.is_valid():
                new_CommentForm.save()
                return redirect("boards:post_detail", pk=pk)
    
    new_CommentForm = CommentForm()
    return render(request, 'boards/post_detail.html', {'post': post,"comment_list" : post_comment_list,"comment_form" : new_CommentForm, "post_pk" : pk})
    
def boards_delete_comment(request,comment_pk):
    if request.user.is_authenticated:
        if request.method == "POST":
            try:
                post_comment = Comment.objects.get(id=comment_pk) #쿼리셋을 얻는다.
                if post_comment.user_id_id == request.user.id: # *_id : db의 fk의 raw value에 접근한다.
                    # if post_comment.user_id_char == request.user.username:
                    reverse_post_pk = post_comment.post_id_id
                    post_comment.delete()
                    return redirect("boards:post_detail", pk=reverse_post_pk) 
            except:
                pass
            
    return redirect("/")

def boards_delete_post(request,post_pk):
    if request.user.is_authenticated:
        if request.method == "POST":
            try:
                post = Post.objects.get(id=post_pk) #쿼리셋을 얻는다.
                if post.user_id_id == request.user.id: # *_id : db의 fk의 raw value에 접근한다.
                    post.delete()
                    return redirect("boards:index")
            except:
                pass
            
    return redirect("/")

def boards_update_post(request,post_pk):
    if request.user.is_authenticated:
        if request.method == "POST":
            try:
                post = Post.objects.get(id=post_pk) #쿼리셋을 얻는다.
                if post.user_id_id == request.user.id: # *_id : db의 fk의 raw value에 접근한다.
                    post_val = PostForm({
                        "user_id" : request.user.id,
                        "user_id_char" : request.user.username,
                        "title" : request.POST.get("title"),
                        "content" : request.POST.get("content"),
                        "updated_bool" : False,
                        "visible_bool" : True,
                    })
                                
                    if post_val.is_valid():
                        post.title = post_val.cleaned_data["title"]
                        post.content = post_val.cleaned_data["content"]
                        post.updated_bool = True
                        
                        post.save()
                        return redirect("boards:post_detail", pk=post_pk) 
            except:
                pass
        else:
            try:
                post = get_object_or_404(Post, pk=post_pk)
            except:
                return redirect("/")
            
            return render(request, 'boards/update_post.html', {'post': post})
            
    return redirect("/")

def boards_update_comment(request,comment_pk):
    if request.user.is_authenticated:
        if request.method == "POST":
            try:
                post_comment = Comment.objects.get(id=comment_pk) #쿼리셋을 얻는다.
                if post_comment.user_id_id == request.user.id: # *_id : db의 fk의 raw value에 접근한다.
                    post_comment_val = CommentForm({"post_id" : post_comment.post_id,
                                                    "user_id" : request.user.id,
                                                    "user_id_char" : request.user.username,
                                                    "comment_content" : request.POST.get("comment_content"),
                                                    "updated_bool" : False,
                                                    "visible_bool" : True,
                                                    })
                    
                    if post_comment_val.is_valid():
                        reverse_post_pk = post_comment.post_id_id
                        
                        post_comment.comment_content = post_comment_val.cleaned_data["comment_content"]
                        post_comment.updated_bool = True
                        
                        post_comment.save()
                        
                        return redirect("boards:post_detail", pk=reverse_post_pk) 
            except:
                pass
            
    return redirect("/")