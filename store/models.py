from django.db import models
from django.urls import reverse
from .utils import generate_slug


class Product(models.Model):

    """ Product implementation """

    title = models.CharField(max_length=150, verbose_name="Наименование")
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(max_length=5000, null=True, verbose_name="Описание")
    image = models.ImageField(verbose_name="Изображение")
    price = models.IntegerField(verbose_name="Цена")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail_url', kwargs={'slug': self.slug})

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


class Sale(models.Model):

    """ sale implementation """

    title = models.CharField(max_length=150, verbose_name="Название")
    image = models.ImageField(verbose_name="Баннер")  # 900x350

