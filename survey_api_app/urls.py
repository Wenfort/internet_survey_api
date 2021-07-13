from django.urls import path
from survey_api_app import views

app_name = 'survey_api_app'
urlpatterns = [
    path('log/', views.login, name='login')
]