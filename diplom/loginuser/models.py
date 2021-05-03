from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    img = models.TextField(verbose_name="Фото сотрудника")
    position = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.user}"

