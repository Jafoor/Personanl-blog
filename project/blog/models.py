from django.db import models

from django.contrib.auth.models import User

from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class AuthorProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 50)
    photo = models.ImageField(upload_to = 'author/')
    about = models.TextField()
    gender_choice = (
        ('male','Male'),
        ('female','Female'),
        ('other','Others')
    )
    gender = models.CharField(choices = gender_choice, max_length = 10)
    facebook_url = models.URLField(null=True, blank=True)
    twitter_url = models.URLField(null=True, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)
    skype_url = models.URLField(null=True, blank=True)
    github_url = models.URLField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class PostCategory(models.Model):
    name = models.CharField(max_length=120, unique=True)
    photo = models.ImageField(upload_to='category/')
    about = models.TextField()
    author = models.ForeignKey(AuthorProfile, on_delete=models.SET_NULL, null=True)
    is_draft = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)
    author = models.ForeignKey(AuthorProfile, on_delete=models.SET_NULL, null=True)
    is_draft = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=245, unique=True)
    urltitle = models.CharField(max_length=100, unique=True)
    blogType = (
        ('english','English'),
        ('bangla','Bangla')
    )
    language = models.CharField(choices = blogType, max_length = 20)
    photo = models.ImageField(upload_to='post/')
    shortTxt = models.TextField()
    content = RichTextUploadingField()
    category = models.ForeignKey(PostCategory, on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField(Tag)
    author = models.ForeignKey(AuthorProfile, on_delete=models.SET_NULL, null=True)
    is_draft = models.BooleanField(default=False)
    pub_date = models.DateField(auto_now_add=True)
    date = models.DateTimeField(auto_now_add=True)
    show = models.IntegerField(default = 0)

    def __str__(self):
        return self.urltitle
