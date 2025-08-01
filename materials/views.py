from django.db.models.expressions import result
from pyexpat.errors import messages
from rest_framework import response
from rest_framework.status import HTTP_200_OK
from kombu.asynchronous.http import Response
from rest_framework.decorators import action, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView, get_object_or_404,
)


from materials.models import Course, Lesson, Subscribing
from materials.pagination import CustomPagination
from materials.serializers import CourseSerializer, LessonSerializer
from materials.tasks import update_course_info
from users.permissions import IsModer, IsOwner
from materials.tasks import update_course_info
from users.serializers import SubscribeSerializer


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

    def perform_update(self, serializer):
        update_course = serializer.save()
        update_course_info.delay(update_course)
        update_course.save()



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


class SubscribingCreateAPIView(CreateAPIView):
    queryset = Subscribing.objects.all()
    serializer_class = SubscribeSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        course_id = request.data.get("course")
        course = get_object_or_404(Course, pk=course_id)
        sub_is = Subscribing.objects.filter(user=user, course=course)
        if sub_is.exists():
            sub_is.delete()
            message = "Подписка удалена"
        else:
            Subscribing.objects.create(user=user, course=course, sign_up=True)
            message = "Подписка добавлена"
        return Response({"message": message})
