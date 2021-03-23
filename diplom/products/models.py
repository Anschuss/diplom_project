from django.db import models
from django.utils.text import slugify


# Оборудывание

class CharacteristicsProduct(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=120, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Area(CharacteristicsProduct):
    pass


class Brand(CharacteristicsProduct):
    pass


class Type(CharacteristicsProduct):
    pass


class Product(models.Model):
    name = models.CharField(max_length=120, unique=True, verbose_name="Название")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Бренд")
    area = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name="Область применения")
    type_product = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name="Тип")
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.brand} {self.type_product} {self.area} {self.name}')
        super(Product, self).save(*args, **kwargs)


class MassageCouch(Product):
    height = models.PositiveIntegerField(default=48)
    size = models.CharField(max_length=32)
    weight_limit = models.PositiveIntegerField(default=100)
    material = models.CharField(max_length=120)
    height_adjustment = models.BooleanField()
    electric_motor = models.BooleanField()


class CharacteristicsLibra(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class TypeLibra(CharacteristicsLibra):
    pass


class Units(CharacteristicsLibra):
    pass


class Screen(CharacteristicsLibra):
    pass


class BabyScales(Product):
    type_libra = models.ForeignKey(TypeLibra, on_delete=models.CASCADE, verbose_name="Тип")
    weight_limit = models.PositiveIntegerField(verbose_name="Максимальный вес")
    discreteness = models.PositiveIntegerField(verbose_name="Дискретность")
    cuvette = models.CharField(max_length=120, default="съёмная", verbose_name="Кювета")
    automatic = models.BooleanField(default="Есть", verbose_name="Автоматическое отключение")
    units = models.ForeignKey(Units, on_delete=models.PROTECT, verbose_name="Еденица измерения")
    screen = models.ForeignKey(Screen, on_delete=models.PROTECT, verbose_name="Экран")
    zero_function = models.BooleanField(default=False, verbose_name="Функция обнкления")
    fixing_weight_value = models.BooleanField(default=False, verbose_name="Фиксация значения веса независимо от движений")
    difference = models.BooleanField(default=False, verbose_name="Разница в весе между взвешиваниями")
    tara_compensation = models.BooleanField(default=False, verbose_name="Тарокомпенсация")
    low_battery_indicator = models.BooleanField(default=False, verbose_name="Индикатор низкого заряда")
    weight = models.PositiveIntegerField(verbose_name="Вес")