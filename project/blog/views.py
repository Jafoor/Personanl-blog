from django.shortcuts import render , get_object_or_404, redirect
from .models import *
from comment.models import *
from django.contrib import messages
# Create your views here.

def home(request):

    return render(request, 'index.html')

def about(request):

    return render(request, 'about.html')

def englishblog(request):

    news = Post.objects.filter(language='english').order_by('-pk')

    return render(request, 'englishblog.html',{'news' : news})

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

    return render(request, 'blogdetails.html',{'detail':detail,'comments':comments,'site':site,'popularpost':popularpost})

def contact(request):

    return render(request, 'contact.html')
