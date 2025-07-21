from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson
from users.models import User, Subscribe

class CourseTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test@yandex.com')
        self.course = Course.objects.create(title='test_course', description='test_description', owner=self.user)
        self.lesson = Lesson.objects.create(title='test_lesson', course=self.course, owner=self.user)
        self.subscribe = Subscribe.objects.create(course=self.course, user=self.user)
        self.client.force_authenticate(user=self.user)


    def test_course_retrieve(self):
        url = reverse('materials:course-detail', args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.course.title)

    def test_course_create(self):
        url = reverse('materials:course-list')
        data = {
            "title": "test_title",
            "link": "https://www.youtube.com/"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


