from django.shortcuts import render

def index(req):
    return  render(req, 'home/index.html')

def login(req):
    return  render(req, 'home/login.html')

def sign_up(req):
    return  render(req, 'home/sign_up.html')