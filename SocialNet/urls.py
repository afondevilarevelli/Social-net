from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from SocialNet.views import main, home

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', main.index),
    path('login', main.login),
    path('signup', main.sign_up),
    path('logout', main.logout),

    path('home', home.index)
]

urlpatterns += staticfiles_urlpatterns()