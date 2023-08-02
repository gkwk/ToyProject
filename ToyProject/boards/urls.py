from django.urls import path, include,reverse_lazy

import boards.views
import boards.forms

urlpatterns = [
    path('', boards.views.boards_index, name='index'),
    path('posting/', boards.views.boards_posting, name='posting'),
    path('post/<int:pk>/', boards.views.boards_post_detail, name='post_detail'),
    path('post_delete/<int:post_pk>/', boards.views.boards_delete_post, name='delete_post'),
    path('post_update/<int:post_pk>/', boards.views.boards_update_post, name='update_post'),
    path('comment_delete/<int:comment_pk>/', boards.views.boards_delete_comment, name='delete_comment'),
    path('comment_update/<int:comment_pk>/', boards.views.boards_update_comment, name='update_comment'),
]

