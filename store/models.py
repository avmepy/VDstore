from django.contrib.auth.models import User
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
        return reverse('product_detail', kwargs={'product_id': self.id})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = generate_slug(self.title)
        super().save(*args, **kwargs)

    def get_characteristics(self):
        """
        returned all characteristics of the object
        :return: dict
        """
        characteristics = {
            "title": self.title,
            "description": self.description,
            "image": self.image,
            "price": self.price,
            "brand": self.brand,
        }

        return characteristics


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

    def get_characteristics(self):

        """
        returned all characteristics of the object
        :return: dict
        """

        characteristics = super(SmartPhone, self).get_characteristics()
        characteristics["water resist"] = self.water_resist
        characteristics["weight"] = self.weight
        characteristics["color"] = self.color
        characteristics["display type"] = self.display_type
        characteristics["display diagonal"] = str(self.display_diagonal)
        characteristics["main_camera"] = self.main_camera
        characteristics["front_camera"] = self.front_camera
        characteristics["cpu"] = self.cpu
        characteristics["ram"] = self.ram
        characteristics["ssd"] = self.ssd
        characteristics["system"] = self.system

        return characteristics


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


class Comment(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:15]

    class Meta:
        ordering = ('-pub_date',)
