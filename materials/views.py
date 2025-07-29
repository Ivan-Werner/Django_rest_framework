from django.db.models.expressions import result
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)


from materials.models import Course, Lesson
from materials.pagination import CustomPagination
from materials.serializers import CourseSerializer, LessonSerializer
from users.permissions import IsModer, IsOwner
from .tasks import add


def my_view(request):
    result = add.delay()  # запускаем задачу
    try:
        hello_world = result.get(timeout=10)
        print(hello_world)
    except TimeoutError:
        print("Задача не завершилась вовремя")


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer



    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [
                ~IsModer,
            ]
        elif self.action in ["update", "retrieve"]:
            self.permission_classes = [
                IsModer | IsOwner,
            ]
        elif self.action == "destroy":
            self.permission_classes = [
                ~IsModer | IsOwner,
            ]
        return super().get_permissions()





class LessonCreateAPIView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [~IsModer, IsAuthenticated]


class LessonListAPIVView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = CustomPagination


class LessonRetrieveAPIView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModer | IsOwner]


class LessonUpdateAPIView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModer | IsOwner]


class LessonDestroyAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwner | ~IsModer]
