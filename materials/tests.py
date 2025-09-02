from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson
from users.models import User, Subscribe


class CourseTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test@yandex.com', is_staff=True, is_superuser=True)
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
            "course": self.course.pk,
            "link_to_video": "https://www.youtube.com/"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.all().count(), 2)

    # def test_course_update(self):
    #     url = reverse('materials:course-detail', args=(self.course.pk,))
    #     data = {
    #         "title": "test_title_updated"
    #     }
    #     response = self.client.patch(url, data)
    #     data = response.json()
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(data.get("title"), "test_title_updated")

    def test_course_delete(self):
        url = reverse('materials:course-detail', args=(self.course.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Course.objects.all().count(), 0)

    def test_course_list(self):
        url = reverse('materials:course-list')
        response = self.client.get(url)
        data = response.json()
        res = data[0]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res), 7)

    def test_subscribe(self):
        url = reverse("users:subscribe-check", args=(self.course.pk,))
        data = {"id": self.course.pk}

        response = self.client.post(url, data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("message"), "Подписка удалена")


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test@yandex.com', is_staff=True, is_superuser=True)
        self.course = Course.objects.create(title='test_course', description='test_description', owner=self.user)
        self.lesson = Lesson.objects.create(title='test_lesson', course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse('materials:lesson-retrieve', args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('title'), self.lesson.title)

    def test_lesson_create(self):
        url = reverse('materials:lesson-create')
        data = {'title': 'test_title',
                'course': self.course.id,
                'link_to_video': 'https://www.youtube.com/'
                }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        url = reverse('materials:lesson-update', args=(self.lesson.pk, ))
        data = {'title': 'test_title_update'}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('title'), 'test_title_update')

    def test_lesson_delete(self):
        url = reverse('materials:lesson-delete', args=(self.lesson.pk, ))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        url = reverse('materials:lesson-list')
        response = self.client.get(url)
        data = response.json()
        res = len(data['results'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(res, 1)
