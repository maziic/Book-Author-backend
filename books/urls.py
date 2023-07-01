# books/urls.py

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AuthorViewSet, BookViewSet, PageViewSet

app_name = "books"

router = DefaultRouter()
router.register(r"authors", AuthorViewSet)
router.register(r"books", BookViewSet)
router.register(r"books/(?P<book_id>\d+)/pages", PageViewSet)

urlpatterns = [
    path("", include(router.urls)),
]