from django.urls import path
from users.apps import UsersConfig
from users import views

app_name = UsersConfig.name


urlpatterns = [
    path('user/update/<int:pk>/', views.UserUpdateAPIView.as_view(), name='user-update'),
    path('user/create/', views.UserCreateAPIView.as_view(), name='user-create'),
    path('user/delete/<int:pk>/', views.UserDeleteAPIView.as_view(), name='user-delete'),
    path('', views.UserListAPIView.as_view(), name='user-list'),
    path('user/<int:pk>/', views.UserRetrieveAPIView.as_view(), name='user-detail'),
]

