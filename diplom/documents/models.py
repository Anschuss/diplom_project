from django.db import models


## Documents


class TenderType(models.Model):
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Clinic(models.Model):
    name = models.CharField(max_length=120, unique=True)
    state = models.BooleanField(default=True)
    address = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}, {self.state}"


class Sale(models.Model):
    class Meta:
        abstract = True

    customer = models.CharField(max_length=120, verbose_name="Заказчик")
    document = models.FileField(verbose_name="Документ")
    price = models.PositiveIntegerField()
    slug = models.SlugField(unique=True)
    guarantee = models.PositiveIntegerField(default=0)
    product = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return f"{self.customer}, {self.price}, {self.product}"


class RetailSales(Sale):
    guarantee_status = models.BooleanField(default=True)


class TenderDoc(Sale):
    organizer = models.CharField(max_length=240, verbose_name="Организатор закупки")
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, blank=False, null=False, verbose_name="Клиника")
    type_tender = models.ForeignKey(TenderType, on_delete=models.CASCADE, blank=True, verbose_name="Тип тендера")
