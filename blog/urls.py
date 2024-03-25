
from . import views
from django.urls import path


app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:post_id>/', views.blog_post_view, name='post_view'),


]

