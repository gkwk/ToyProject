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
    #         else:
    #             new_CommentForm = CommentForm()
    #             return render(request, 'notice_detail.html', {'post': post,"comment_list" : post_comment_list,"comment_form" : new_CommentForm, "post_pk" : pk})
            
    #     else:
    #         new_CommentForm = CommentForm()
    #         return render(request, 'notice_detail.html', {'post': post,"comment_list" : post_comment_list,"comment_form" : new_CommentForm, "post_pk" : pk})
        
    # else:
    #     return render(request, 'notice_detail.html', {'post': post, "comment_list" : post_comment_list,})
    
    new_CommentForm = CommentForm()
    return render(request, 'boards/post_detail.html', {'post': post,"comment_list" : post_comment_list,"comment_form" : new_CommentForm, "post_pk" : pk})
    
def boards_delete_comment(request,comment_pk):
    if request.user.is_authenticated:
        if request.method == "POST":
            try:
                notice_comment = Comment.objects.get(id=comment_pk) #쿼리셋을 얻는다.
                if notice_comment.user_id_id == request.user.id: # *_id : db의 fk의 raw value에 접근한다.
                    if notice_comment.user_id_char == request.user.username:
                        reverse_notice_pk = notice_comment.post_id_id
                        notice_comment.delete()
                        return redirect("boards:post_detail", pk=reverse_notice_pk) 
            except:
                pass
            
    return redirect("/")




# def new_posting(request):
#     # if request.user.is_authenticated:
#     if request.user.is_superuser:
#         if request.method == "GET":
#             return render(request, 'new_posting.html')
        
#         elif request.method == "POST":
#             new_post = Notice_post()
#             new_post.uploader_id = request.user.username
#             new_post.text = request.POST.get('editorTxt')
#             new_post.title = request.POST.get('title')
            
#             up_time = timezone.datetime.now()
#             new_post.upload_date = up_time
#             new_post.date_text = datetime.date.strftime(up_time, '%Y년 %m월 %d일 %H:%M:%S') 
#             new_post.save()
#             return redirect('notice:notice')

#         return render(request, 'new_posting.html')
#     else:
#         return redirect('/')
    
# def notice_detail(request,pk):
#     post = get_object_or_404(Notice_post, pk=pk)
    
#     notice_comment_list = Comment.objects.filter(post_id=pk).values("id","user_id","user_id_char","comment_body","created_date","updated_date") #쿼리셋을 얻는다.
#     notice_comment_list = list(notice_comment_list) #쿼리셋을 리스트화한다.
        
#     if request.user.is_authenticated:
#         if request.method == "POST":
#             new_CommentForm = CommentForm(request.POST)
                        
#             if new_CommentForm.is_valid():

#                 new_CommentForm = CommentForm({"post_id" : pk, "user_id" : request.user.id, "user_id_char" : request.user.username ,"comment_body" : new_CommentForm.cleaned_data["comment_body"]})
#                 new_CommentForm.is_valid()
#                 new_CommentForm.save()
#                 return redirect("notice:notice_detail", pk=pk)
#             else:
#                 new_CommentForm = CommentForm()
#                 return render(request, 'notice_detail.html', {'post': post,"comment_list" : notice_comment_list,"comment_form" : new_CommentForm, "post_pk" : pk})
            
#         else:
#             new_CommentForm = CommentForm()
#             return render(request, 'notice_detail.html', {'post': post,"comment_list" : notice_comment_list,"comment_form" : new_CommentForm, "post_pk" : pk})
        
#     else:
#         return render(request, 'notice_detail.html', {'post': post, "comment_list" : notice_comment_list,})
        
# def notice_comment_delete(request,comment_pk):
#     if request.user.is_authenticated:
#         if request.method == "POST":
#             try:
#                 notice_comment = Comment.objects.get(id=comment_pk) #쿼리셋을 얻는다.
#                 if notice_comment.user_id_id == request.user.id: # *_id : db의 fk의 raw value에 접근한다.
#                     if notice_comment.user_id_char == request.user.username:
#                         reverse_notice_pk = notice_comment.post_id_id
#                         notice_comment.delete()
#                         return redirect("notice:notice_detail", pk=reverse_notice_pk) 
#             except:
#                 pass
            
#     return redirect("/")