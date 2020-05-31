from django.shortcuts import render , get_object_or_404, redirect
from .models import *
# Create your views here.

def home(request):

    return render(request, 'index.html')

def about(request):

    return render(request, 'about.html')

def englishblog(request):

    news = Post.objects.filter(language='english').order_by('-pk')

    return render(request, 'englishblog.html',{'news' : news})

def blogdetails(request,word):

    detail = Post.objects.get(urltitle = word)
    print(detail)

    return render(request, 'blogdetails.html',{'detail':detail})
