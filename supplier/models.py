from django.db import models
from users.models import User
from django.utils.timezone import now

NULLABLE = {'null': True, 'blank': True}


class Supplier(models.Model):
    """Поставщик"""
    RANK = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2')
    )
    SUPPLIER_TYPE = (
        ('factory', 'Завод'),
        ('retail', 'Розничная сеть'),
        ('entrepreneur', 'Индивидуальный предприниматель')
    )
    CURRENCY = (
        ('RUB', 'Российский рубль'),
        ('USD', 'Доллар США'),
        ('EUR', 'Евро'),
        ('CNY', 'Юань'),
        ('BYN', 'Белорусский рубль'),
        ('UAH', 'Гривна'),
        ('TRY', 'Турецкая лира')
    )

    name = models.CharField(unique=True, max_length=150, verbose_name='Название')
    time_of_creation = models.DateTimeField(default=now, verbose_name='Время создания')
    previous_supplier = models.ForeignKey('Supplier', on_delete=models.SET_NULL,
                                          verbose_name='Поставщик оборудования', **NULLABLE)
    ranking = models.CharField(max_length=15, choices=RANK, verbose_name='Уровень иерархии', **NULLABLE)
    supplier_type = models.CharField(max_length=15, choices=SUPPLIER_TYPE, verbose_name='Тип поставщика')

    email = models.EmailField(unique=True, verbose_name='Почта')
    country = models.CharField(max_length=150, verbose_name='Страна')
    city = models.CharField(max_length=150, verbose_name='Город')
    street = models.CharField(max_length=150, verbose_name='Улица')
    house_number = models.CharField(max_length=50, verbose_name='Номер дома')

    debt_amount = models.FloatField(verbose_name='Сумма задолженности перед поставщиком')
    debt_type = models.CharField(max_length=15, choices=CURRENCY, verbose_name='Валюта')

    def __str__(self):
        return f'{self.name} '

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
        ordering = ('name',)


class Product(models.Model):
    """ Продукт """
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='Владелец')
    name = models.CharField(max_length=150, verbose_name='Название')
    model = models.CharField(max_length=200, verbose_name='Модель')
    launch_date = models.DateTimeField(default=now, verbose_name='Дата выхода продукта на рынок')
    image = models.ImageField(upload_to='electronic_shop_dinn/supplier', verbose_name='Изображение', **NULLABLE)
    price = models.FloatField(verbose_name='Цена в РУБ',  **NULLABLE)

    def __str__(self):
        return f'{self.name} '

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)
