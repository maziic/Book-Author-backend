from django.contrib import admin

# Register your models here.
# books/admin.py

from django.contrib import admin

from .models import Author, Book, Page

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Page)