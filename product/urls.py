
from django.urls import path
from django.conf import settings # NEW
from. import views


app_name = 'product'
urlpatterns = [

path('', views.home, name='home'),
path('post/<int:post_id>/', views.product_post_view, name='prod_view'),
]


