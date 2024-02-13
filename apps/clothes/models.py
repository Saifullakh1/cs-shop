from django.db import models
from apps.categories.models import Category


class Clothes(models.Model):
    class Currency(models.TextChoices):
        som = "C"
        dollar = "$"
        euro = "€"

    class Size(models.TextChoices):
        m = "M"
        l = "L"
        xl = "XL"
    title = models.CharField(
        max_length=250, verbose_name="Название"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to="clothes_images", verbose_name="Картинка"
    )
    size = models.CharField(
        max_length=150, choices=Size.choices,
        default=Size.l, verbose_name="Размер"
    )
    price = models.IntegerField(
        default=0, verbose_name="Цена"
    )
    old_price = models.IntegerField(
        default=0, verbose_name="Старая цена"
    )
    currency = models.CharField(
        max_length=150, choices=Currency.choices,
        default=Currency.som, verbose_name="Валюта"
    )
    is_active = models.BooleanField(
        default=True, verbose_name="Активный"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name="cloth_category", verbose_name="Категория"
    )

    class Meta:
        verbose_name = "Одежда"
        verbose_name_plural = "Одежды"

    def __str__(self):
        return self.title
