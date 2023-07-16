from django.urls import path, include

import account.views

urlpatterns = [
    path("login/",account.views.login_view,name="login"),
    path("logout/",account.views.logout_view,name="logout"),
    path("register/",account.views.register_view,name="register"),
    path("register_complete/",account.views.register_complete_view,name="register_complete"),
]
