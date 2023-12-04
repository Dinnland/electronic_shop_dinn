# Generated by Django 4.2.7 on 2023-12-04 00:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название')),
                ('time_of_creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время создания')),
                ('ranking', models.CharField(blank=True, choices=[('0', '0'), ('1', '1'), ('2', '2')], max_length=15, null=True, verbose_name='Уровень иерархии')),
                ('supplier_type', models.CharField(choices=[('factory', 'Завод'), ('retail', 'Розничная сеть'), ('entrepreneur', 'Индивидуальный предприниматель')], max_length=15, verbose_name='Тип поставщика')),
                ('image', models.ImageField(blank=True, null=True, upload_to='electronic_shop_dinn/supplier', verbose_name='Изображение')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Почта')),
                ('country', models.CharField(max_length=150, verbose_name='Страна')),
                ('city', models.CharField(max_length=150, verbose_name='Город')),
                ('street', models.CharField(max_length=150, verbose_name='Улица')),
                ('house_number', models.CharField(max_length=50, verbose_name='Номер дома')),
                ('launch_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата выхода продукта на рынок')),
                ('debt_amount', models.FloatField(verbose_name='Сумма задолженности перед поставщиком')),
                ('debt_type', models.CharField(choices=[('RUB', 'Российский рубль'), ('USD', 'Доллар США'), ('EUR', 'Евро'), ('CNY', 'Юань'), ('BYN', 'Белорусский рубль'), ('UAH', 'Гривна'), ('TRY', 'Турецкая лира')], max_length=15, verbose_name='Валюта')),
                ('previous_supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='supplier.supplier', verbose_name='Поставщик оборудования')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('model', models.CharField(max_length=200, verbose_name='Модель')),
                ('launch_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата выхода продукта на рынок')),
                ('image', models.ImageField(blank=True, null=True, upload_to='electronic_shop_dinn/supplier', verbose_name='Изображение')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplier.supplier', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ('name',),
            },
        ),
    ]