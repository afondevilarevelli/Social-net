from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from SocialNet.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.index),
    path('login', home.login),
    path('signup', home.sign_up)
]

urlpatterns += staticfiles_urlpatterns()