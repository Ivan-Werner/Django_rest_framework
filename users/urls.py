from django.urls import path
from rest_framework.permissions import AllowAny

from users.apps import UsersConfig
from users import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = UsersConfig.name


urlpatterns = [
    path(
        "user/update/<int:pk>/", views.UserUpdateAPIView.as_view(), name="user-update"
    ),
    path("register/", views.UserCreateAPIView.as_view(), name="register"),
    path(
        "user/delete/<int:pk>/", views.UserDeleteAPIView.as_view(), name="user-delete"
    ),
    path("", views.UserListAPIView.as_view(), name="user-list"),
    path("user/<int:pk>/", views.UserRetrieveAPIView.as_view(), name="user-detail"),
    path("payments/", views.PaymentListAPIView.as_view(), name="payment"),
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=[AllowAny]),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=[AllowAny]),
        name="token_refresh",
    ),
]
