from django.db import models

# Create your models here.
# books/models.py

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

class Author(models.Model):
    name = models.CharField(_("Author name"), max_length=100)
    bio = models.TextField(_("Author bio"))

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(_("Book title"), max_length=250)
    author = models.ForeignKey(
        Author,
        related_name="books",
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ("-id",)

    def __str__(self):
        return f"{self.title} by {self.author.name}"

class Page(models.Model):
    book = models.ForeignKey(Book, related_name="pages", on_delete=models.CASCADE)
    content = models.TextField(_("Page content"))

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return f"Page {self.id} of {self.book.title}"