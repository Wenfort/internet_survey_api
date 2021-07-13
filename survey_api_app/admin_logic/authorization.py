from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.response import Response


class AuthenticationHandler:

    def __init__(self, request):
        self.username = request.data.get("username")
        self.password = request.data.get("password")
        self.user = object()

        self.error_message = str()
        self.error_status = str()

    def get_token(self):
        if self._is_data_valid():
            token = Token.objects.get_or_create(user=self.user)[0]
            return Response({'token': token.key},
                            status=HTTP_200_OK)

    def _is_data_valid(self):
        if self._is_data_not_empty() and self._is_existing_user():
            return True

    def _is_data_not_empty(self):
        if self.username and self.password:
            return True

        self.error_message = 'Пожалуйста, введите имя пользователя и пароль'
        self.error_status = HTTP_400_BAD_REQUEST

    def _is_existing_user(self):
        self.user = authenticate(username=self.username, password=self.password)

        if self.user:
            return True

        self.error_message = 'Логин и пароль не соответствуют ни одной учетной записи'
        self.error_status = HTTP_404_NOT_FOUND
