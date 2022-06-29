from rest_framework import permissions


class IsCurrentUserOrReadOnly(permissions.BasePermission):
    '''Class to construct a custom permissions to check if the user have rights to update,delete an object'''

    def has_object_permission(self, request, view, obj):
        if request.method is permissions.SAFE_METHODS:
            return True
        else:
            return obj.user == request.user


        
