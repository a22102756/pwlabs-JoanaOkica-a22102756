from django.contrib import admin
from .models import Author, Post, Coment

# Register your models here.
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Coment)
