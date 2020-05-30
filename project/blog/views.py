from django.shortcuts import render , get_object_or_404, redirect

# Create your views here.

def home(request):

    return render(request, 'index.html')

def about(request):

    return render(request, 'about.html')

def englishblog(request):

    return render(request, 'englishblog.html')

def blogdetails(request):

    return render(request, 'blogdetails.html')
