from django.db import models


## Products

class BrandProduct(models.Model):
    brand = models.CharField(max_length=120, unique=True)


class TypeProduct(models.Model):
    name = models.CharField(max_length=120, unique=True)


class Product(models.Model):
    name = models.CharField(max_length=120)
    type = models.ForeignKey(TypeProduct, on_delete=models.CASCADE)
    brand = models.ForeignKey(BrandProduct, on_delete=models.CASCADE)


## Documents

class Clinic(models.Model):
    name = models.CharField(max_length=120, unique=True)
    state = models.BooleanField(default=True)


class Sale(models.Model):
    class Meta:
        abstract = True

    customer = models.CharField(max_length=120, verbose_name="Заказчик")
    document = models.ImageField(verbose_name="Документ")
    price = models.PositiveIntegerField()
    slug = models.SlugField(unique=True)
    guarantee = models.PositiveIntegerField(default=0)
    product = models.ManyToManyField(Product)


class RetailSales(Sale):
    guarantee_status = models.BooleanField(default=True)


class TenderDoc(Sale):
    organizer = models.CharField(max_length=240, verbose_name="Организатор закупки")
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, blank=False, null=False, verbose_name="Клиника")
