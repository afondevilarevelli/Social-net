from django.shortcuts import render, redirect
from db.models import Post

def index(req):
    if req.COOKIES.get('user_cookie'):
        modelView = {
            "posts": Post.objects.filter(owner=req.COOKIES.get('user_cookie')).order_by('date')
        }
        return render(req, 'home/index.html', context=modelView)
    else:
        return redirect('/')

def profile(req):
    if req.COOKIES.get('user_cookie'):
        return render(req, 'home/profile.html')
    else:
        return redirect('/')