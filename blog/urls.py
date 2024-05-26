
from . import views
from django.urls import path

app_name = 'blog'
urlpatterns = [
   
    

    path('', views.home, name='home'),
    path('post/<int:post_id>/', views.salon_detail, name='post_view'),
    path('post/add/', views.add_salon, name='post-add'),
    path('post/<int:post_id>/change/', views.changer_salon, name='post-change'),
    path('post/<int:post_id>/delete/', views.delete_salon, name='post-delete'),
    path('post/<int:post_id>/publish/', views.saloon_publish, name='post-publish'),
    path('search_salon/', views.search_salon, name='search_salon'),

    path('post/<int:post_id>/favori/', views.ajouter_favoris, name='ajouter_favoris'),
   
    path('product/', views.home_prod, name='home_prod'),
    path('product/<int:product_id>/', views.product_detail, name='prod_view'),
    path('product/add/', views.add_product, name='product-add'),
    path('search_produit/', views.search_produit, name='search_produit'),
    

    path('evaluation/<int:post_id>/', views.home_evaluation, name='home_evaluation'),
    path('post/<int:post_id>/addEvaluation/', views.evaluer_salon, name='add-evaluation'),
    
    path('count/', views.liste_salons, name='count'),
]