# books/permissions.py

from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Check if authenticated user is the author of the book or page.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # Assuming the book or page has an 'author' foreign key field
        if hasattr(obj, 'author'):
            return obj.author == request.user

        return False