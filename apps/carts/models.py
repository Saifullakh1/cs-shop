from django.db import models

from apps.clothes.models import Clothes
from apps.users.models import User


class Cart(models.Model):
    clothes_id = models.ForeignKey(
        Clothes, on_delete=models.CASCADE,
        related_name="cart_clothes", verbose_name="Одежда"
    )
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="cart_users", verbose_name="Пользователь"
    )

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f"{self.user_id} - {self.clothes_id}"