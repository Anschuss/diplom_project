from django.db import models
from django.utils.text import slugify
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse


class LatestDoxManager:

    @staticmethod
    def get_doc_for_page(*args, **kwargs):
        dox = []
        ct_models = ContentType.objects.filter(model__in=args)
        for ct_model in ct_models:
            model_doc = ct_model.model_class()._base_manager.all().order_by('id')
            dox.extend(model_doc)
        return dox


class LatestDox:
    object = LatestDoxManager


## Documents

class TenderCharacteristics(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=120, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class TypeProduct(TenderCharacteristics):
    pass


class StatusTender(TenderCharacteristics):
    pass


class TenderType(TenderCharacteristics):
    pass


class Clinic(TenderCharacteristics):
    state = models.BooleanField(default=True, verbose_name="Государственная клиника")
    address = models.CharField(max_length=200, unique=True, verbose_name="Адрес клиники")

    def __str__(self):
        return f"{self.name}, {self.state}"


class Sale(models.Model):
    class Meta:
        abstract = True

    number_contract = models.CharField(max_length=64, unique=True, verbose_name="Номер договора")
    customer = models.CharField(max_length=120, verbose_name="Заказчик")
    document = models.FileField(verbose_name="Документ")
    price = models.PositiveIntegerField(verbose_name="Цена")
    slug = models.SlugField(unique=True)
    guarantee = models.PositiveIntegerField(default=0, verbose_name="Гарантийный срок")
    type_product = models.ForeignKey(TypeProduct, on_delete=models.CASCADE, verbose_name="тип мед услуг")
    product = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return f"{self.customer}, {self.price}, {self.product}"

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.customer} {self.price} {self.guarantee} {self.number_contract}')
        super().save(*args, **kwargs)


class RetailSales(Sale):
    def get_absolute_url(self):
        return reverse("doc:tenders", kwargs={"ct_model": "retailsales", "slug": self.slug})


class TenderDoc(Sale):
    organizer = models.CharField(max_length=240, verbose_name="Организатор закупки")
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, blank=False, null=False, verbose_name="Клиника")
    type_tender = models.ForeignKey(TenderType, on_delete=models.CASCADE, blank=True, verbose_name="Тип тендера")
    status = models.ForeignKey(StatusTender, on_delete=models.PROTECT, blank=True, verbose_name="Статус тендера")
    description = models.TextField(blank=True, verbose_name="Описание")

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.organizer} {self.clinic} {self.type_tender} {self.number_contract}')
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("doc:tenders", kwargs={"ct_model": "tenderdoc", "slug": self.slug})
