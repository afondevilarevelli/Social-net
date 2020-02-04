from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from login import views as login
from main_menu import views as main_menu

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', login.index),
    path('login', login.login),
    path('signup', login.sign_up),
    path('logout', login.logout),

    path('home', main_menu.index),
    path('profile', main_menu.profile)
]

urlpatterns += staticfiles_urlpatterns()