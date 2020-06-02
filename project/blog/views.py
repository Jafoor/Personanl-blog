from django.shortcuts import render , get_object_or_404, redirect
from .models import *
from comment.models import *
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def home(request):

    latest = Post.objects.filter().order_by('-pk')[:3]
    all = Post.objects.all().count()
    english = Post.objects.filter(language='english').count()
    bangla = Post.objects.filter(language='bangla').count()
    cat = PostCategory.objects.all().count()
    site = SiteSettings.objects.get(name='sitesettings')

    return render(request, 'index.html',{'latest':latest,'all':all,'english':english,'bangla':bangla,'cat':cat,'site':site})

def about(request):

    site = SiteSettings.objects.get(name='sitesettings')

    return render(request, 'about.html',{'site':site})

def englishblog(request):

    news = Post.objects.filter(language='english').order_by('-pk')

    allcat = PostCategory.objects.filter(language='english')
    cats = { }
    for i in allcat:
        total = Post.objects.filter(category=i).count()
        cats[i] = total

    site = SiteSettings.objects.get(name='sitesettings')

    paginator = Paginator(news,10)
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except EmptyPage:
        news = paginator.page(paginator.num_page)
    except PageNotAnInteger:
        news = paginator.page(1)

    return render(request, 'englishblog.html',{'news' : news,'cats':cats,'site':site})


def banglablog(request):

    news = Post.objects.filter(language='bangla').order_by('-pk')

    allcat = PostCategory.objects.filter(language='bangla')
    cats = { }
    for i in allcat:
        total = Post.objects.filter(category=i).count()
        cats[i] = total
    site = SiteSettings.objects.get(name='sitesettings')

    paginator = Paginator(news,10)
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except EmptyPage:
        news = paginator.page(paginator.num_page)
    except PageNotAnInteger:
        news = paginator.page(1)


    return render(request, 'banglablog.html',{'news' : news,'cats':cats,'site':site})



def blogdetails(request,word):
    print(word)
    detail = Post.objects.get(urltitle=word)
    print(1)
    popularpost = Post.objects.filter(language = 'english').order_by('-show')[:5]
    print(popularpost)
    view = detail.show
    view += 1
    print(view)
    detail.show = view
    detail.save()
    site = SiteSettings.objects.get(name='sitesettings')

    related = Post.objects.filter(category=detail.category).exclude(urltitle=word)


    #Catgories
    allcat = PostCategory.objects.filter(language='english')
    cats = { }
    for i in allcat:
        total = Post.objects.filter(category=i).count()
        cats[i] = total


    comments = Comment.objects.filter(post = word).order_by('pk')

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('message')

        if name == "" or comment == "":
            messages.error(request, 'name or message is empty')
            return redirect('blogdetails', word=word)
        else:
            b = Comment(name = name, email = email, comment = comment, post = word)
            b.save()
            messages.error(request, 'Successfully added comment')
            return redirect('blogdetails', word=word)

    return render(request, 'blogdetails.html',{'detail':detail,'comments':comments,'site':site,'popularpost':popularpost,'related':related,'cats':cats})

def contact(request):

    site = SiteSettings.objects.get(name='sitesettings')
    return render(request, 'contact.html',{'site':site})

def category(request):

    cat = PostCategory.objects.filter(language='english')
    posts = Post.objects.filter(language = 'english').order_by('category')
    news = Post.objects.filter().order_by('-pk')
    site = SiteSettings.objects.get(name='sitesettings')


    paginator = Paginator(news,10)
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except EmptyPage:
        news = paginator.page(paginator.num_page)
    except PageNotAnInteger:
        news = paginator.page(1)

    return render(request, 'category.html',{'cat':cat,'posts':posts,'news':news,'site':site})
