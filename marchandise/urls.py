
from . import views
from django.urls import path


app_name = 'marchandise'
urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:post_id>/', views.marchandise_post_view, name='post_view'),
    path('post/add/', views.march_post_add, name='post-add'),
    path('post/<int:post_id>/change/', views.march_post_change, name='post-change'),
    path('post/<int:post_id>/delete/', views.march_post_delete,name= 'post-delete'),
    path('post/<int:post_id>/publish/', views.march_post_publish, name= 'post-publish'),

   ]

