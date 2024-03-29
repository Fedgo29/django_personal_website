from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('posts/', views.posts, name="posts"),
    path('post/<str:pk>', views.post, name="post"),
    path('profile/', views.profile, name="profile"),


    path('send_email/', views.sendEmail, name="send_email"),

]