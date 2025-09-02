from rest_framework.fields import SerializerMethodField, URLField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson, Subscribing
from materials.validators import validate_not_forbidden


class LessonSerializer(ModelSerializer):
    link_to_video = URLField(validators=[validate_not_forbidden])

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    lesson_count = SerializerMethodField()
    link_to_video = URLField(validators=[validate_not_forbidden])
    lessons = LessonSerializer(many=True, read_only=True)

    def get_lesson_count(self, obj):
        return obj.lessons.count()

    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "lessons",
            "preview",
            "description",
            "link_to_video",
            "lesson_count",
        ]


class SubscribingSerializer(ModelSerializer):
    class Meta:
        model = Subscribing
        fields = "__all__"
