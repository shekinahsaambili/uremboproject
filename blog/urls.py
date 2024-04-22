
from . import views
from django.urls import path


app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:post_id>/', views.blog_post_detail, name='post_view'),
    path('post/add/', views.blog_post_add, name='post-add'),
    path('post/<int:post_id>/change/', views.blog_post_change, name='post-change'),
    path('post/<int:post_id>/delete/', views.blog_post_delete,name= 'post-delete'),
    path('post/<int:post_id>/publish/', views.blog_post_publish, name= 'post-publish'),
]

