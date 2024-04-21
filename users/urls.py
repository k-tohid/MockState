from django.urls import path

from .views import (
    CustomUserListCreateAPIView,
    CustomUserDetailAPIView,
    LoginAPIView
)


urlpatterns = [
    path("", view=CustomUserListCreateAPIView.as_view()),
    path("login/", view=LoginAPIView.as_view()),
    path("<str:username>/", view=CustomUserDetailAPIView.as_view()),
]
