
from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$',views.home, name = 'home'),
    url(r'^about/$',views.about, name = 'about'),
    url(r'^englishblog/$',views.englishblog, name = 'englishblog'),
    url(r'^blogdetails/(?P<word>[\w\+]+)/$',views.blogdetails, name = 'blogdetails'),
    ]
