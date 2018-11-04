from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    # blog:index: list all posts
    path('', views.PostListView.as_view(), name='index'),

    # blog:post-detail: post's detail
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),

    # blog:post-create: create a post
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),

    # blog:post-update: update a post
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(),
        name='post-update'),

    # blog:post-delete: delete a post
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(),
        name='post-delete'),

    # blog:user_posts: user's posts
    path('user/<str:username>/', views.UserPostListView.as_view(),
        name='user-posts'),

    # blog:about: about page
    path('about/', views.about, name='about'),

    #
]
