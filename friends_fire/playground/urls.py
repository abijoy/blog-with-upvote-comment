
from django.urls import path
from . import views
from django.contrib.auth import login, logout
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('signup/', views.SignUp, name='signup'),
	path('accounts/login/', auth_views.LoginView.as_view(), {'template_name': 'playground/login.html'}, name='login'),
	path('accounts/logout/', auth_views.LogoutView.as_view(), {'template_name': 'playground/logout.html'}, name='logout'),
	path('', views.home, name='home'),
	path('post/<int:post_id>/', views.post_details, name='post_details'),
	path('post/upvote/<int:post_id>/', views.upvote, name='upvote'),
	path('post/add/', views.addPost, name='addPost'),
	path('post/unvote/<int:post_id>/', views.unvote, name='unvote'),
	path('post/upvoted-by/<int:post_id>/', views.upvoted_by, name='upvoted_by'),
	path('make_comment/<int:post_id>/', views.make_comment, name='make_comment'),
	path('find-lyrics/', views.find_lyrics, name='find_lyrics'),
]