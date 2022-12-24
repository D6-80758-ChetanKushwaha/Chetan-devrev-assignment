from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='user-home'),
    path('login/',auth_views.LoginView.as_view(template_name="cineplex_user/login.html"),name='user-login'),
    path('profile/',views.profile,name='user-profile'),
    path('signout/',auth_views.LogoutView.as_view(template_name="cineplex_user/logout.html"),name='user-logout'),
    path('signup/',views.signup,name='user-signup'),
]
