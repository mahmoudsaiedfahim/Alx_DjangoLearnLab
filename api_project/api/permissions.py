from rest_framework.permissions import BasePermission

class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.mothod in ['GET','HEAD','OPTIONS']:
            return True
        return obj.author == request.user