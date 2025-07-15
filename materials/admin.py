from django.contrib import admin

from materials.models import Course, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'preview', 'description')
    search_fields = ('title', )
    search_filter = ('title', )


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'preview', 'link_to_video')
    search_fields = ('title', )
    search_filter = ('title', )
