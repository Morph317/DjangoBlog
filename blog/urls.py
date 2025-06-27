from django.urls import path
from .views import HomeView, PostDetailView, CreatePostView, UpdatePostView, DeletePostView

urlpatterns = [
    #path("", views.home, name="home"),
    path("", HomeView.as_view(), name="home"),
    path("post/<int:pk>", PostDetailView.as_view(), name="post-detail"), #pk: Primary Key 是Django数据库自带的索引
    path("submit", CreatePostView.as_view(), name="create-post"),
    path("post/edit/<int:pk>", UpdatePostView.as_view(), name="edit-post"),
    path("post/delete/<int:pk>", DeletePostView.as_view(), name="delete-post"),

]
