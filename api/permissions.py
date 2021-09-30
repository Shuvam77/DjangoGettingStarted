from rest_framework import permissions


class IsOrganizerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        # readonly permission are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the organizer of the meeting
        return obj.organizer == request.user
