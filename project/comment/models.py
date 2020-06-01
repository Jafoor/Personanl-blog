from django.db import models

# Create your models here.

class Comment(models.Model):

    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 100)
    comment = models.TextField()
    post = models.CharField(max_length = 200, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class SiteSettings(models.Model):

    name = models.CharField(max_length=100, default = 'sitesettings')

    email = models.EmailField(max_length = 100)
    fb = models.URLField(null=True, blank=True)
    tw = models.URLField(null=True, blank=True)
    gh = models.URLField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    mypic1 = models.ImageField(upload_to = 'sitesettings/%Y/%m/%d' , blank=True)
    mypic2 = models.ImageField(upload_to = 'sitesettings/%Y/%m/%d' , blank=True)
    mypic3 = models.ImageField(upload_to = 'sitesettings/%Y/%m/%d' , blank=True)
    mypic4 = models.ImageField(upload_to = 'sitesettings/%Y/%m/%d' , blank=True)
    loge = models.ImageField(upload_to = 'sitesettings/%Y/%m/%d' , blank=True)

    def __str__(self):
        return self.email
