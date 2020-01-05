from django.shortcuts import render, redirect
from db.models import User 
from django.http import Http404, HttpResponse, JsonResponse

def index(req):
    if req.COOKIES.get('user_cookie'):
        return redirect('/home')
    else:
        return render(req, 'main/index.html')

def login(req):
    if req.POST:
        try:
            user = User.objects.get(username = req.POST['username'], password = req.POST['password'])
            res = JsonResponse({"message": "Succesful logged in"})
            res.set_cookie('user_cookie', user.id)
            res.status_code = 200
            return res
        except Exception:
            res = JsonResponse({"error": "Username and password doesn't match"})
            res.status_code = 400
            return res
    else:
        return render(req, 'main/login.html')


def logout(req):
    res = redirect('/')
    res.delete_cookie('user_cookie')
    return res

def sign_up(req):
    if req.POST:
        if(req.POST['username'] == ''):
            raise Http404("Username cannot be empty")
        if(req.POST['password'] != req.POST['password2']):
            raise Http404("Passwords didn't match")

        new_user = User.objects.create(
            username = req.POST['username'],
            password = req.POST['password'],
            name = req.POST['first_name'],
            lastname = req.POST['lastname'],
            birthday = req.POST['birthday'],
            mail = req.POST['mail'],
            icon =  req.POST['image'] if req.POST['image'] else None
        )
        res = redirect('/home')
        res.set_cookie('user_cookie', new_user.id)
        return res
    else:
        return render(req, 'main/sign_up.html')