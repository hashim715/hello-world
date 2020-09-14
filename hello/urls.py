"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from bestproducts.views import Postview,Detailview,AddPost,UpdatePost,DeletePost
urlpatterns = [
    path("post/", Postview.as_view(),name="post"),
    path("admin/", admin.site.urls),
    path('article/<int:pk>', Detailview.as_view(), name="article"),
    path('add_post/', AddPost.as_view(), name='add_blog'),
    path("update_post/edit/<int:pk>",UpdatePost.as_view(), name="update_post"),
    path("new_page/<int:pk>", DeletePost.as_view(), name="delete_post"),
]
