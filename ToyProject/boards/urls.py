from django.urls import path, include,reverse_lazy

import boards.views
import boards.forms

urlpatterns = [
    path('', boards.views.boards_index, name='index'),
    path('posting/', boards.views.boards_posting, name='posting'),
    path('notice/<int:pk>/', boards.views.boards_post_detail, name='post_detail'),
    path('comment_delete/<int:comment_pk>/', boards.views.boards_delete_comment, name='delete_comment'),
]

