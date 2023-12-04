from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from supplier.models import Supplier, Product
from users.models import User


# Create your tests here.

class ProductTestCase(APITestCase):
    client_class = APIClient

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
        self.supplier2 = Supplier.objects.create(
            name='ИП Егоров Д. Г.',
            supplier_type='entrepreneur',
            email='egorov@mail.com',
            country='Россия',
            city='Казань',
            street='Декабристов',
            house_number='54',
            debt_amount='20000.0',
            debt_type='RUB',
            previous_supplier=self.supplier1
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
        self.user2.is_active = False
        self.user2.set_password('12345678')
        self.user2.save()

        self.data1 = {
            'supplier': self.supplier1,
            'name': 'Смартфон redmi',
            'model': 'Note 12',
            'price': '14000'
        }

        self.product = Product.objects.create(**self.data1)
        self.client.force_authenticate(user=self.user1)

    def test_get_list(self):
        """GET-запрос Активного пользователя"""
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(path='/supplier/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_list2(self):
        """GET-запрос Неактивного пользователя"""
        self.client.force_authenticate(user=self.user2)
        response = self.client.get(path='/supplier/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_supplier2(self):
        """Через API не происходит обновление задолженности"""
        self.client.force_authenticate(user=self.user1)
        new_debt_amount = '0'
        data = {'debt_amount': new_debt_amount}
        response = self.client.patch(path=f'/supplier/{self.supplier2.pk}/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.supplier2.refresh_from_db()
        self.assertNotEqual(self.supplier2.debt_amount, new_debt_amount)

    def test_delete_supplier1(self):
        """Обычные пользователи не имеют права удалять Поставщика"""
        self.client.force_authenticate(user=self.user1)
        response = self.client.delete(path=f'/supplier/{self.supplier1.pk}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
