from django.urls import path

from .views import (
    CustomUserListAPIView,
    CustomUserCreateAPIView,
    CustomUserDetailAPIView,
    CustomUserUpdateAPIView,
    CustomUserDeleteAPIView,
    LoginAPIView
)


# urlpatterns = [
#     path("", view=CustomUserListCreateAPIView.as_view(), name='create-list-user'),
#     path("login/", view=LoginAPIView.as_view()),
#     path("<str:username>/", view=CustomUserDetailAPIView.as_view()),
# ]


urlpatterns = [
    path("", view=CustomUserListAPIView.as_view(), name='user_list'),
    path("create/", view=CustomUserCreateAPIView.as_view(), name='user_create'),
    path('<str:username>/', view=CustomUserDetailAPIView.as_view(), name='user_detail'),
    path('<str:username>/update/', view=CustomUserUpdateAPIView.as_view(), name='user_update'),
    path('<str:username>/delete/', view=CustomUserDeleteAPIView.as_view(), name='user_delete'),
    path("login/", view=LoginAPIView.as_view(), name='user_login'),
]
