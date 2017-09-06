from django import forms
from django.contrib import admin

from .fields import UserSelectWidget

from .models import Post


class BlogForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = []
        widgets = {
            'author': UserSelectWidget,
        }


class BlogAdmin(admin.ModelAdmin):
    form = BlogForm

admin.site.register(Post, BlogAdmin)
# Register your models here.
