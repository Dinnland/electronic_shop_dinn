from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from supplier.models import Supplier, Product
from users.models import User


# Create your tests here.

class ProductTestCase(APITestCase):
    client_class = APIClient
    # def setUp(self) -> None:
    #     self.user = User.objects.create(email='test@for1.ru', password='0000')
    #
    # def test_create_lesson(self):
    #     """тест соз урока"""
    #     data = {
    #         "name": "nameoflesson",
    #         "description": "descrrr",
    #         'owner': self.user
    #     }
    #     response = self.client.post(
    #         '/lesson/create/',
    #         data=data,
    #     )
    #
    #     print(response.json())
    #
    #     self.assertEqual(
    #         response.status_code,
    #         status.HTTP_201_CREATED
    #     )
    def setUp(self) -> None:
        # self.url = '/'
        # self.url = reverse('supplier')
        self.supplier1 = Supplier.objects.create(
            name='Завод Электроники имени Ленина',
            supplier_type='factory',
            email='zeil@mail.com',
            country='Россия',
            city='Казань',
            street='Декабристов',
            house_number='59/1',
            debt_amount='0.0',
            debt_type='RUB'
        )

        self.user1 = User.objects.create(
            email='test@1user.ru',
        )
        self.user1.set_password('12345678')
        self.user1.is_active = 'True'
        self.user1.save()

        self.user2 = User.objects.create(
            email='test@2user.ru',
        )
        self.user2.is_active = 'False'
        self.user2.set_password('12345678')
        self.user2.save()


        self.data1 = {
            'supplier': self.supplier1,
            'name': 'Смартфон redmi',
            'model': 'Note 12',
            'price': '14000'
        }

        self.data1 = {
            'supplier': self.supplier1,
            'name': 'Смартфон redmi',
            'model': 'Note 12',
            'price': '14000'
        }

        self.product = Product.objects.create(**self.data1)
        self.client.force_authenticate(user=self.user1)

    # def test_create_product(self):
    #     data = {
    #         'name': 'testT',
    #         'description': 'test',
    #         'course': self.course.pk,
    #         'owner': self.user.pk
    #     }
    #     lesson_create_url = reverse('course_app:lesson-create')
    #     response = self.client.post(lesson_create_url, data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Lesson.objects.all().count(), 2)

    def test_get_list(self):
        # Тестирование GET-запроса к API
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(path='/supplier/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_list2(self):
        # Тестирование GET-запроса к API
        self.client.force_authenticate(user=self.user2)
        print(self.user2.is_active)
        response = self.client.get(path='/supplier/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_detail_lesson(self):
#         lesson_detail_url = reverse('course_app:lesson-retrieve', kwargs={'pk': self.lesson.pk})
#         response = self.client.get(lesson_detail_url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['name'], self.lesson.name)
#
#     def test_update_lesson(self):
#         lesson_update_url = reverse('course_app:lesson-update', kwargs={'pk': self.lesson.pk})
#         new_name = 'new_name'
#         data = {'name': new_name}
#         response = self.client.patch(lesson_update_url, data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.lesson.refresh_from_db()
#         self.assertEqual(self.lesson.name, new_name)
#
#     def test_delete_lesson(self):
#         lesson_delete_url = reverse('course_app:lesson-delete', kwargs={'pk': self.lesson.pk})
#         response = self.client.delete(lesson_delete_url)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertFalse(Lesson.objects.filter(pk=self.lesson.pk).exists())
#
#
# class SubscriptionsTestCase(APITestCase):
#     def setUp(self) -> None:
#         self.course = Course.objects.create(name='test', description='desc')
#         self.user = User.objects.create(email='test@user.ru', password='0000')
#         self.data = {
#             'user': self.user,
#             'course': self.course,
#         }
#
#         self.subscription = Subscription.objects.create(**self.data)
#         self.client.force_authenticate(user=self.user)
#
#     def test_create_subscription(self):
#         data = {
#             'user': self.user.pk,
#             'course': self.course.pk,
#         }
#         subscription_url = reverse('course_app:course-subscribe')
#         print(subscription_url)
#         response = self.client.post(subscription_url, data)
#         print(response)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         # self.assertEqual(Subscription.objects.all().count(), 2)
