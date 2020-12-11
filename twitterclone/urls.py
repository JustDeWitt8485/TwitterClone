"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from twitteruser import views


urlpatterns = [
    path('', views.index, name='homepage'),
    path('addtweet/', views.add_tweet, name='addtweet'),
    path('signup/', views.sign_up, name='signup'),
    path('profile/<int:author_id>/', views.profile_view, name='profilepage'),
    path('tweet/<int:tweet_id>/', views.tweet_view, name='tweetpage'),
    path('follow/<int:author_id>/', views.follow_view),
    path('login/', views.login_view, name='loginpage'),
    path('logout/', views.logout_view, name='logoutpage'),
    path('admin/', admin.site.urls),
]
