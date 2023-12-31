"""
URL configuration for ToyProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin

import ToyProject.views

urlpatterns = [
    path("admin/", admin.site.urls,name="admin"),
    path("",ToyProject.views.index,name="index"),
    path("header/",ToyProject.views.header,name="header"),
    
    #include
    path("account/",include(("account.urls","account"),namespace="account")),
    path("services/",include(("services.urls","services"),namespace="services")),
    path("boards/",include(("boards.urls","boards"),namespace="boards")),
    path("ORM/",include(("ORM.urls","ORM"),namespace="ORM")),
]
