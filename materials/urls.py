from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from materials.views import CourseViewSet, LessonCreateAPIView, LessonListAPIVView, LessonRetrieveAPIView, LessonUpdateAPIView, LessonDestroyAPIView
from materials.apps import MaterialsConfig

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path('lesson/', LessonListAPIVView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_retrieve'),
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/<int:pk>/delete/', LessonDestroyAPIView.as_view(), name='lesson_delete'),
]

urlpatterns += router.urls
