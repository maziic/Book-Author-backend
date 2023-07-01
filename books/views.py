from django.shortcuts import render

# Create your views here.
# books/views.py

from django.shortcuts import get_object_or_404
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Author, Book, Page
from .serializers import AuthorSerializer, BookSerializer, PageSerializer
from .permissions import IsAuthorOrReadOnly



class AuthorViewSet(viewsets.ModelViewSet):
    """
    CRUD authors
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get_permissions(self):
        if self.action in ("list", "retrieve"):
            self.permission_classes = (permissions.AllowAny,)
        elif self.action in ("create",):
            self.permission_classes = (permissions.IsAuthenticated,)
        else:
            self.permission_classes = (IsAuthorOrReadOnly,)

        return super().get_permissions()


class BookViewSet(viewsets.ModelViewSet):
    """
    CRUD books
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.action in ("list", "retrieve"):
            self.permission_classes = (permissions.AllowAny,)
        elif self.action in ("create",):
            self.permission_classes = (permissions.IsAuthenticated,)
        else:
            self.permission_classes = (IsAuthorOrReadOnly,)

        return super().get_permissions()

class PageViewSet(viewsets.ModelViewSet):
    """
    CRUD pages for a particular book
    """
    queryset = Page.objects.all()
    serializer_class = PageSerializer

    def get_queryset(self):
        res = super().get_queryset()
        book_id = self.kwargs.get("book_id")
        return res.filter(book__id=book_id)

    def get_permissions(self):
        if self.action in ("list", "retrieve"):
            self.permission_classes = (permissions.AllowAny,)
        elif self.action in ("create",):
            self.permission_classes = (permissions.IsAuthenticated,)
        else:
            self.permission_classes = (IsAuthorOrReadOnly,)

        return super().get_permissions()