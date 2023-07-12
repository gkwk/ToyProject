from django.urls import path, include

import register.views

urlpatterns = [
    path("",register.views.index,name="index"),
]