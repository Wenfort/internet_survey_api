from django.urls import path
from rest_framework.routers import SimpleRouter

from survey_api_app import views
from survey_api_app.views import SurveyViewSet, QuestionViewSet, ActiveSurveyViewSet, ChoiceViewSet, RespondentChoiceViewSet

router = SimpleRouter()
router.register(r'survey', SurveyViewSet)
router.register(r'question', QuestionViewSet)
router.register(r'choice', ChoiceViewSet)
router.register(r'active_survey', ActiveSurveyViewSet)
router.register(r'user_choice', RespondentChoiceViewSet)

app_name = 'survey_api_app'
urlpatterns = [
    path('log/', views.login, name='login'),
]

urlpatterns += router.urls
print(router.urls)
