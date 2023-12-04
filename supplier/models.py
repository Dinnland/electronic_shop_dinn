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

    # owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name='Создатель')
    name = models.CharField(unique=True, max_length=150, verbose_name='Название')
    time_of_creation = models.DateTimeField(default=now, verbose_name='Время создания')
    previous_supplier = models.ForeignKey('Supplier', on_delete=models.SET_NULL,
                                          verbose_name='Поставщик оборудования', **NULLABLE)
    ranking = models.CharField(max_length=15, choices=RANK, verbose_name='Уровень иерархии', **NULLABLE)
    supplier_type = models.CharField(max_length=15, choices=SUPPLIER_TYPE, verbose_name='Тип поставщика')
    # electronic_shop
    # image = models.ImageField(upload_to='electronic_shop_dinn/supplier', verbose_name='Изображение', **NULLABLE)
    # debt_amount = models.FloatField(verbose_name='Задолженность перед поставщиком', default=0)

    email = models.EmailField(unique=True, verbose_name='Почта')
    country = models.CharField(max_length=150, verbose_name='Страна')
    city = models.CharField(max_length=150, verbose_name='Город')
    street = models.CharField(max_length=150, verbose_name='Улица')
    house_number = models.CharField(max_length=50, verbose_name='Номер дома')
    launch_date = models.DateTimeField(default=now, verbose_name='Дата выхода продукта на рынок')

    debt_amount = models.FloatField(verbose_name='Сумма задолженности перед поставщиком')
    debt_type = models.CharField(max_length=15, choices=CURRENCY, verbose_name='Валюта')

    def __str__(self):
        return f'{self.name} '

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
        ordering = ('name',)

    # objects = UserManager()


class Product(models.Model):
    """ Продукт """
    # supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE,)

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




# class Contacts(models.Model):
#     """ Контакты """
#     supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE,)
#     email = models.EmailField(unique=True, verbose_name='Почта')
#     country = models.CharField(max_length=150, verbose_name='Страна')
#     city = models.CharField(max_length=150, verbose_name='Город')
#     street = models.CharField(max_length=150, verbose_name='Улица')
#     house_number = models.CharField(max_length=50, verbose_name='Номер дома')
#     launch_date = models.DateTimeField(default=now, verbose_name='Дата выхода продукта на рынок')
#
#     def __str__(self):
#         return f'{self.email} '
#
#     class Meta:
#         verbose_name = 'Контакты'
#         verbose_name_plural = 'Контакты'
#         ordering = ('email',)


# class Debt(models.Model):
#     """Задолженность"""
#     CURRENCY = (
#         ('RUB', 'Российский рубль'),
#         ('USD', 'Доллар США'),
#         ('EUR', 'Евро'),
#         ('CNY', 'Юань'),
#         ('BYN', 'Белорусский рубль'),
#         ('UAH', 'Гривна'),
#         ('TRY', 'Турецкая лира'),
#     )
#     creditor = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='Кредитор', related_name='creditor')
#     debtor = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='должник', related_name='debtor')
#     debt_amount = models.FloatField(verbose_name='Сумма задолженности')
#     debt_type = models.CharField(max_length=15, choices=CURRENCY, verbose_name='Валюта')
#
#     class Meta:
#         verbose_name = 'Задолженность'
#         verbose_name_plural = 'Задолженности'
#         ordering = ('debtor',)