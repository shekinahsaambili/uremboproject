from django.urls import path

from . import views

app_name = 'pages'
urlpatterns = [
     path('',views.index, name='index'),
   path('account/',views.account, name='account'),
    path('apropos/',views.apropos, name='apropos'),
]
