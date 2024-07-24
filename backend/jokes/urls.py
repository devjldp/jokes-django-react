from django.urls import path
from . import views


urlpatterns = [
    path('api/jokes/', views.JokeListCreate.as_view()),
]
