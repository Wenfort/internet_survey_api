import datetime
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Respondent, Survey, Question, Choice, RespondentAnswer
from .serializer import SurveySerializer, SurveySerializerWithBlockedStartDay, QuestionSerializer, ChoiceSerializer, \
    RespondentAnswerSerializer, UserMakesChoiceSerializer
from .admin_logic.authorization import AuthenticationHandler


@api_view(["GET"])
def login(request):
    auth_handler = AuthenticationHandler(request)
    return auth_handler.get_token() or Response({'error_message': auth_handler.error_message},
                                                status=auth_handler.error_status)


class SurveyViewSet(ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.request.method == 'PUT':
            serializer_class = SurveySerializerWithBlockedStartDay

        return serializer_class


class ActiveSurveyViewSet(SurveyViewSet):
    date_now = datetime.date.today()
    queryset = Survey.objects.filter(end_date__gte=date_now, start_date__lte=date_now).select_related()


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ChoiceViewSet(ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class RespondentChoiceViewSet(ModelViewSet):
    queryset = Respondent.objects.all()
    serializer_class = RespondentAnswerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class UserMakesChoiceViewSet(ModelViewSet):
    queryset = RespondentAnswer.objects.all()
    serializer_class = UserMakesChoiceSerializer
