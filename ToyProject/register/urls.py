from django.urls import path, include

import register.views

urlpatterns = [
    path("",register.views.register,name="register"),
    path("modal/",register.views.modal,name="modal"),
]