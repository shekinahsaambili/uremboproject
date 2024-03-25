
from django.urls import path
from django.conf import settings # NEW
from. import views


app_name = 'salon'
urlpatterns = [

path('', views.home, name='home'),
path('post/<int:post_id>/', views.salon_post_view, name='post_view'),
]


