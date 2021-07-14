from django.urls import path
from rest_framework.routers import SimpleRouter
from survey_api_app import views
from survey_api_app.views import SurveyViewSet, QuestionViewSet, ActiveSurveyViewSet, ChoiceViewSet, \
    RespondentChoiceViewSet, UserMakesChoiceViewSet

router = SimpleRouter()
router.register(r'survey', SurveyViewSet)
router.register(r'question', QuestionViewSet)
router.register(r'choice', ChoiceViewSet)
router.register(r'active_survey', ActiveSurveyViewSet)
router.register(r'user_choice', RespondentChoiceViewSet)
router.register(r'user_makes_choice', UserMakesChoiceViewSet)

urlpatterns = [
    path('log/', views.login, name='login'),
]

urlpatterns += router.urls