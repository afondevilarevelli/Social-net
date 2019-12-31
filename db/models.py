from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(unique=True, max_length=30)
    password = models.TextField()
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    birthday = models.DateField()
    mail = models.EmailField()
    icon = models.ImageField(blank=True, upload_to='SocialNet/static/temp-images')
    friends = models.ManyToManyField("self", related_name='friends', blank=True, default=None, null=True)

class Post(models.Model):
    text = models.CharField(max_length=500)
    date = models.DateTimeField()
    image = models.ImageField(blank=True, upload_to='SocialNet/static/temp-images')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    likes = models.ManyToManyField(User, related_name='likes', blank=True, default=None, null=True)