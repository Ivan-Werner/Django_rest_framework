from django.contrib import admin

from materials.models import Course, Lesson, Subscribing


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "preview", "description")
    search_fields = ("title",)
    search_filter = ("title",)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "preview", "link_to_video")
    search_fields = ("title",)
    search_filter = ("title",)


@admin.register(Subscribing)
class SubscribingAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "sign_up")
    search_fields = ("sign_up", "user")
    search_filter = ("sign_up", "user")
