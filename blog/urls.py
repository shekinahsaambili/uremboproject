
from . import views
from django.urls import path

app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.home_prod, name='home_prod'),
    path('post/<int:post_id>/', views.salon_detail, name='post_view'),
    path('product/<int:product_id>/', views.product_detail, name='prod_view'),
    path('post/add/', views.add_salon, name='post-add'),
    path('product/add/', views.add_product, name='product-add'),
    path('post/<int:post_id>/change/', views.changer_salon, name='post-change'),
    path('post/<int:post_id>/delete/', views.delete_salon, name='post-delete'),
    path('post/<int:post_id>/publish/', views.blog_post_publish, name='post-publish'),
]