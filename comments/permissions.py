from rest_framework.permissions import BasePermission


class CommentPermission(BasePermission):
    def has_permission(self, request, view):
        """
        Define si un usuario puede ejecutar cierto método o acceder a cierta vista/controlador.
        Args:
            request:
            view: vista que se está ejecutando
        Returns: True si el usuario puede acceder
        """

        ## only authenticated users can create a comment:
        # if request.method == "POST" and request.user.is_authenticated(): #doesn't work
        if request.method == "POST" and request.user.authenticated:
            return True

        if request.method == "GET":
            return True

        ## the rest, without permissions
        return False


    def has_object_permission(self, request, view, obj):
        """
        Define si un usuario puede realizar la operación que quiere sobre el objeto obj
        :param request:
        :param view: vista que se está ejecutando
        :param obj: objeto al que se quiere acceder
        :return: True si el usuario puede realizar la acción
        """
        return request.user.is_superuser or request.user == obj
