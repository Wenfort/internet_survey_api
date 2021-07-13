from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from .admin_logic.authorization import AuthenticationHandler


@api_view(["GET"])
def login(request):
    auth_handler = AuthenticationHandler(request)
    return auth_handler.get_token() or Response({'error_message': auth_handler.error_message}, status=auth_handler.error_status)


