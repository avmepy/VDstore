from django.db import models
from django.urls import reverse
from .utils import generate_slug

import sys
sys.path.append("..")
from account.models import Profile, User


class Product(models.Model):

    """ Product implementation """

    title = models.CharField(max_length=150, verbose_name="Наименование")
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(max_length=5000, null=True, verbose_name="Описание")
    image = models.ImageField(verbose_name="Изображение")
    price = models.IntegerField(verbose_name="Цена")
    brand = models.CharField(verbose_name="Бренд", max_length=150)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = generate_slug(self.title)
        super().save(*args, **kwargs)


class SmartPhone(Product):

    """smartphone implementations (extends from product)"""

    water_resist = models.CharField(verbose_name="Стандарт защиты от воды", max_length=50)
    weight = models.IntegerField(verbose_name="Вес")
    color = models.CharField(verbose_name="Цвет", max_length=50)
    display_type = models.CharField(verbose_name="Тип экрана", max_length=50)
    display_diagonal = models.FloatField(verbose_name="Диагональ экрана")
    main_camera = models.IntegerField(verbose_name="Разрешение основной камеры")
    front_camera = models.IntegerField(verbose_name="Разрешение фронтальной камеры")
    cpu = models.CharField(verbose_name="Процессор", max_length=50)
    ram = models.IntegerField(verbose_name="Оперативная память")
    ssd = models.IntegerField(verbose_name="Встроенная память")
    system = models.CharField(verbose_name="Платформа", max_length=50)


class Laptop(Product):

    """laptop implementation (extends from product)"""

    display_diagonal = models.FloatField(verbose_name="Диагональ экрана")
    display_type = models.CharField(verbose_name="Тип дисплея", max_length=50)
    material = models.CharField(verbose_name="Материал корпуса", max_length=50)
    cpu = models.CharField(verbose_name="Процессор", max_length=50)
    ram = models.IntegerField(verbose_name="Оперативная память")
    mem = models.IntegerField(verbose_name="Встроенная память")
    mem_type = models.CharField(verbose_name="Тип встроенной памяти (SSD/HDD)", max_length=50)
    gpu = models.CharField(verbose_name="Видеокарта", max_length=50)
    gpu_type = models.CharField(verbose_name="Тип видеокарты (Дискретная/Интегрированная)", max_length=50)
    weight = models.IntegerField(verbose_name="Вес")


class Tablet(Product):
    """tablet implementation (extends from product)"""

    weight = models.IntegerField(verbose_name="Вес")
    color = models.CharField(verbose_name="Цвет", max_length=50)
    display_type = models.CharField(verbose_name="Тип экрана", max_length=50)
    display_diagonal = models.FloatField(verbose_name="Диагональ экрана")
    cpu = models.CharField(verbose_name="Процессор", max_length=50)
    ram = models.IntegerField(verbose_name="Оперативная память")
    ssd = models.IntegerField(verbose_name="Встроенная память")
    system = models.CharField(verbose_name="Платформа", max_length=50)


class SmartWatch(Product):
    """smartwatch implementation (extends from product)"""

    sex = models.CharField(verbose_name="Для кого (Мужские/Женские/Унисекс)", max_length=50)
    system = models.CharField(verbose_name="Платформа", max_length=50)
    cpu = models.CharField(verbose_name="Процессор", max_length=50)
    material = models.CharField(verbose_name="Материал корпуса", max_length=50)
    display_type = models.CharField(verbose_name="Тип экрана", max_length=50)
    display_diagonal = models.FloatField(verbose_name="Диагональ экрана")
    weight = models.IntegerField(verbose_name="Вес")


class Audio(Product):
    """audio implementation (extends from product)"""

    audio_type = models.CharField(verbose_name="Тип (Колонки/Наушники)", max_length=50)
    audio_connection_type = models.CharField(verbose_name="Тип (Проводной/Беспроводной/)", max_length=50)
    frequency_range = models.CharField(verbose_name="Диапазон частот (минимальная - максимальная)", max_length=50)
    sensitiveness = models.IntegerField(verbose_name="Чувствительность")
    resistance = models.IntegerField(verbose_name="Сопротивление")
    weight = models.IntegerField(verbose_name="Вес")


class Computer(Product):
    """PC implementation (extends from product)"""

    material = models.CharField(verbose_name="Материал корпуса", max_length=50)
    cpu = models.CharField(verbose_name="Процессор", max_length=50)
    ram = models.IntegerField(verbose_name="Оперативная память")
    mem = models.IntegerField(verbose_name="Встроенная память")
    mem_type = models.CharField(verbose_name="Тип встроенной памяти (SSD/HDD)", max_length=50)
    gpu = models.CharField(verbose_name="Видеокарта", max_length=50)
    gpu_type = models.CharField(verbose_name="Тип видеокарты (Дискретная/Интегрированная)", max_length=50)
    weight = models.IntegerField(verbose_name="Вес")


class TV(Product):
    """tv implementation (extends from product)"""

    pass


class Sale(models.Model):

    """ sale implementation """

    title = models.CharField(max_length=150, verbose_name="Название")
    image = models.ImageField(verbose_name="Баннер")  # 900x350


class Cart(models.Model):

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
