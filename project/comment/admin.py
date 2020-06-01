from django.contrib import admin
from . import models
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'date']
    list_filter = ('post',)


admin.site.register(models.Comment, CommentAdmin)
admin.site.register(models.SiteSettings)
