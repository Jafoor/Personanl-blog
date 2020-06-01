from django.shortcuts import render , get_object_or_404, redirect
from .models import *
from django.contrib import messages

# Create your views here.

def comment(request,word):

    detail = Post.objects.get(urltitle = word)

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('message')

        if name == "" or comment == "":
            messages.error(request, 'name or message is empty')
            return redirect('comment', word=word)


    return render(request, 'blogdetails.html',{'detail':detail})
