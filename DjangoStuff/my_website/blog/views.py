from django.shortcuts import render_to_response, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm
from blog.models import Post

# Create your views here.
def index(request):
    all_posts = Post.objects.all().order_by('-date')
    template_data = {'posts' : all_posts}
    return render_to_response('index.html',template_data)
