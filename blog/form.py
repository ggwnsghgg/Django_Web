from django import forms
from .models import Post
from blog import models
from django.db import models


class BlogUpdate(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "title_image","content", "category"]


# class BlogUpdate(models.Model):
#     class Meta:
#         model = Post
#         fields = ["title", "title_image","content", "category"]