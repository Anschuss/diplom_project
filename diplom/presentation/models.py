from django.db import models
from django.utils.text import slugify


class Status(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name="Статус")
    description = models.TextField(blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name


class Presentation(models.Model):
    number_tender = models.PositiveIntegerField(verbose_name="Номер тендера")
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name="Статус тендера")
    description = models.TextField(blank=True, verbose_name="Описание презентации")
    slug = models.SlugField(unique=True)
    file_presentation = models.FileField(verbose_name="Фаил презентации", upload_to="presentation")

    def __str__(self):
        return f"{self.number_tender}, {self.status}"

    def save(self, *args, **kwargs):
        self.slug = slugify(f'presentation {self.number_tender}')
        super().save(*args, **kwargs)

