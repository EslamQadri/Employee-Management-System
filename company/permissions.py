from rest_framework import permissions

class IsCompanyOwnerOrSuperuser(permissions.BasePermission):
    """
    Custom permission to only allow company owners or superusers to access an endpoint.
    """

    def has_permission(self, request, view):
        # Check if the user is a superuser or a company owner
        return request.user.is_superuser or (
            request.user.employee.company_id == view.kwargs['id'] if 'id' in view.kwargs else False
        )
